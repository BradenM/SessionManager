import React, { Component } from 'react';
import { Icon } from '../elements/icons';
import Input from '../elements/input';
import CircleProgress from '../elements/progress';
import { create_session, get_prog } from '../backend';
import { resolve } from 'path';
const path = require('path');
const electron = window.require('electron');
const { dialog } = electron.remote;

const formatHelp = val => {
  if (val.constructor === Number) {
    return String(val) + '%';
  } else {
    let str = val.constructor === Array ? val[0] : val;
    if (str.includes(path.sep)) {
      var trim = str.split('/');
      str = path.sep + trim[trim.length - 2] + path.sep + trim[trim.length - 1];
    }
    return str;
  }
};

const StepItem = props => {
  let active = props.active ? ' is-active' : '';
  let complete = props.complete ? ' is-completed' : '';
  return (
    <div className={'step-item has-text-light is-link' + active + complete}>
      <div className="step-marker" />
      <div className="step-details">
        <p className="step-title">{props.title}</p>
        <p>{formatHelp(props.help)}</p>
      </div>
    </div>
  );
};

class StepTimeline extends Component {
  renderSteps(steps, current) {
    let render = [];
    for (var key in steps) {
      let item = this.props.steps[key];
      let itemIndex = this.props.steps.indexOf(item);
      let curStep = this.props.steps[current];
      let active = curStep == item;
      let complete = itemIndex < current;
      render.push(
        <StepItem
          key={'step_marker_' + item.title}
          active={active}
          complete={complete}
          title={item.title}
          help={item.value}
        />
      );
    }
    return render;
  }
  render() {
    return (
      <div className="steps">
        {this.renderSteps(this.props.steps, this.props.current)}
      </div>
    );
  }
}

class StepPage extends Component {
  constructor(props) {
    super(props);
    this.renderInput = this.renderInput.bind(this);
    this.renderLoad = this.renderLoad.bind(this);
  }
  renderStep(step) {
    const renderTypes = {
      input: this.renderInput,
      load: this.renderLoad
    };
    let r = renderTypes[step.type];
    return r(step);
  }
  renderInput(step) {
    return (
      <Input
        class="fancy-step"
        label={step.title}
        handleChange={e => this.props.handleChange(e)}
        handleSubmit={() => {
          this.props.handleSubmit();
        }}
        handleClick={e => this.props.handleClick(e)}
        value={step.value}
        helpText={step.helpText}
      />
    );
  }

  renderLoad(step) {
    return (
      <CircleProgress
        style="inner-label"
        percent={step.value}
        title={step.helpText}
      />
    );
  }

  render() {
    return (
      <div className="column is-one-fifth">
        {() => this.props.testCreate()}
        {this.renderStep(this.props.step)}
      </div>
    );
  }
}

class CreateFrame extends Component {
  constructor(props) {
    super(props);
    const steps = [
      {
        title: 'Name',
        value: '',
        helpText: 'Enter a name for your new session',
        has_click: false,
        type: 'input'
      },
      {
        title: 'Path',
        value: '',
        helpText: 'Open your Raw images',
        has_click: true,
        type: 'input'
      },
      {
        title: 'Copy',
        value: 0,
        helpText: 'Copying Files',
        has_click: false,
        type: 'load'
      },
      {
        title: 'Convert',
        value: 0,
        helpText: 'Converting to DNG',
        has_click: false,
        type: 'load'
      }
    ];
    this.state = {
      steps: steps,
      current_step: 0
    };
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
    let curStep = this.state.current_step;
    let session = {
      name: steps[0].value,
      raw_path: steps[1].value[0]
    };
    create_session(session).then((res, error) => {
      // Debug
      console.log('CREATE RES: ', res);
      console.log('CREATE ERROR: ', error);
    });
    this.handleProgress(steps[curStep]);
  }

  handleProgress(step) {
    let steps = this.state.steps.slice();
    let curStep = this.state.current_step;
    get_prog(res => {
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
      if (res !== 100) {
        this.handleProgress(step);
        return;
      }
    });
  }

  handleNext(val) {
    let steps = this.state.steps.slice();
    let curStep = this.state.current_step;
    console.log(steps.length - 3);
    console.log(steps.indexOf(steps[curStep]));
    this.setState({
      steps: steps,
      current_step: curStep // + 1
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
            handleSubmit={e => this.handleNext()}
            handleChange={e => this.handleInput(e)}
            handleClick={e => this.handlePath()}
            testCreate={() => this.handleCreate()}
            step={curStep}
          />
        </div>
        <StepTimeline
          steps={this.state.steps}
          current={this.state.current_step}
        />
      </div>
    );
  }
}

export default CreateFrame;
