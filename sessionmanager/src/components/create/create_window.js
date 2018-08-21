import React, { Component } from 'react';
import { Icon } from '../elements/icons';
import { create_session, get_prog } from '../backend';
import StepTimeline from './timeline';
import StepPage from './step';
import { Exception } from 'utils/validate';
const electron = window.require('electron');
const { dialog } = electron.remote;

class CreateFrame extends Component {
  constructor(props) {
    super(props);
    const steps = [
      {
        title: 'Name',
        value: '',
        helpText: 'Enter a name for your new session',
        has_click: false,
        type: 'input',
        exceptions: [Exception('SessionExists')]
      },
      {
        title: 'Path',
        value: '',
        helpText: 'Open your Raw images',
        has_click: true,
        type: 'input',
        exceptions: [Exception('NoRawFiles')]
      },
      {
        title: 'Copy',
        value: 0,
        helpText: 'Copying Files',
        has_click: false,
        type: 'load',
        request: 'copy',
        exceptions: []
      },
      {
        title: 'Convert',
        value: 0,
        helpText: 'Converting to DNG',
        has_click: false,
        type: 'load',
        request: 'convert',
        exceptions: []
      },
      {
        title: 'Finished',
        value: '',
        helpText: 'Session Created!',
        has_click: false,
        type: 'finish',
        exceptions: []
      }
    ];
    this.status_good = 'GOOD';
    this.state = {
      steps: steps,
      current_step: 0,
      status: this.status_good
    };
    this.handleProgress = this.handleProgress.bind(this);
    this.handleCreate = this.handleCreate.bind(this);
    this.handleError = this.handleError.bind(this);
  }

  handlePath() {
    let steps = this.state.steps.slice();
    let current = steps[this.state.current_step];
    if (current.has_click === false) {
      return;
    }
    let path = dialog.showOpenDialog({
      properties: ['openDirectory'],
      title: 'Choose a folder containing RAW (*.CR2) Files'
    });
    if (path === undefined) {
      return;
    }
    current.value = path;
    this.setState({
      steps: steps
    });
  }

  handleCreate() {
    let steps = this.state.steps.slice();
    let session = {
      name: steps[0].value,
      raw_path: steps[1].value[0]
    };
    create_session(session)
      .then(res => {
        // Debug
        console.log('CREATE RES: ', res);
      })
      .catch(error => {
        console.log('CREATE ERROR: ', error);
        if (error) {
          // True meaning parse and create exception
          let exception = Exception(error, true);
          this.setState({
            status: exception.code
          });
          this.handleError(exception);
          return;
        }
      });
  }

  handleProgress(step) {
    let steps = this.state.steps.slice();
    let curStep = this.state.current_step;
    let step_req = steps[curStep].request;
    if (this.state.status !== this.status_good) {
      return;
    }
    get_prog(step_req, res => {
      // Debug
      console.log('callback res: ', res);
      if (res === undefined || res === null) {
        res = steps[curStep].value;
      } else {
        steps[curStep].value = res;
      }
      this.setState({
        steps: steps
      });
      if (steps[curStep].value === 100) {
        // Next Step if complete
        setTimeout(
          function() {
            this.handleNext();
          }.bind(this),
          300
        );
      } else {
        // Else keep requesting progress
        setTimeout(
          function() {
            this.handleProgress(step);
            return;
          }.bind(this),
          50
        );
      }
    });
  }

  handleNext() {
    let steps = this.state.steps.slice();
    let curStep = this.state.current_step;
    let isDone = steps.indexOf(steps[curStep + 1]) == -1;
    let current_status = this.state.status;
    if (isDone) {
      this.props.toggleCreate();
      return;
    }
    this.setState(
      {
        steps: steps,
        current_step: curStep + 1,
        status: this.status_good
      },
      () => {
        let current = this.state.steps[this.state.current_step];

        if (current.type === 'load') {
          this.handleProgress(current);
          if (current.title === 'Copy' || current_status !== this.status_good) {
            this.handleCreate();
          }
        }
      }
    );
  }

  handleError(error) {
    let steps = this.state.steps.slice();
    let resp_step =
      steps[steps.indexOf(steps.filter(s => s.exceptions.includes(error))[0])];
    resp_step.helpText = error.helpText;
    this.setState({
      steps: steps,
      current_step: steps.indexOf(resp_step)
    });
  }

  handleInput(event) {
    let steps = this.state.steps.slice();
    let current = steps[this.state.current_step];
    if (current.has_click === true) {
      return;
    }
    current.value = event.target.value;
    this.setState({
      steps: steps
    });
  }

  render() {
    let curStep = this.state.steps[this.state.current_step];
    return (
      <div className="frame">
        <div className="exit-window">
          <a
            href="#"
            className="button is-white is-outlined"
            onClick={this.props.toggleCreate}
          >
            <span className="icon is-large">
              <i>{Icon('times', 'lg', '')}</i>
            </span>
            <span>Close</span>
          </a>
        </div>
        <div className="columns is-centered">
          <div className="column">
            <h1 className="has-text-white title is-1">New Session</h1>
          </div>
        </div>
        <div className="columns is-centered has-space-top">
          <StepPage
            key={curStep.label}
            handleSubmit={() => this.handleNext()}
            handleChange={e => this.handleInput(e)}
            handleClick={() => this.handlePath()}
            hasError={this.state.status !== this.status_good}
            step={curStep}
          />
        </div>
        <div className="columns">
          <div className="column step-timeline">
            <StepTimeline
              steps={this.state.steps}
              current={this.state.current_step}
            />
          </div>
        </div>
      </div>
    );
  }
}

export default CreateFrame;
