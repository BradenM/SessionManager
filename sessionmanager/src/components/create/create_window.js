import React, { Component } from 'react';
import { Icon } from '../icons';

const StepItem = props => {
  let active = props.active ? ' is-active' : '';
  let complete = props.complete ? ' is-completed' : '';
  return (
    <div className={'step-item has-text-light is-link' + active + complete}>
      <div className="step-marker" />
      <div className="step-details">
        <p className="step-title">{props.title}</p>
      </div>
    </div>
  );
};

class Steps extends Component {
  renderSteps(steps, current) {
    let render = [];
    for (var key in steps) {
      let item = this.props.steps[key];
      let itemIndex = this.props.steps.indexOf(item);
      let curStep = this.props.steps[current];
      let active = curStep == item;
      let complete = itemIndex < current;
      render.push(
        <StepItem active={active} complete={complete} title={item.title} />
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

class CreateFrame extends Component {
  constructor(props) {
    super(props);
    const steps = [
      {
        title: 'Name',
        content: this.renderName()
      },
      {
        title: 'Path',
        content: this.renderPath()
      }
    ];
    this.state = {
      steps: steps,
      current_step: 0
    };
  }

  renderName() {
    return (
      <div className="column is-one-fifth">
        <div className="control input-control">
          <input
            type="text"
            className="input bottom-border"
            placeholder=""
            required
          />
          <span className="focus-border" />
          <span className="focus-label">Name</span>
          <span
            className="focus-submit"
            onClick={() => {
              this.handleNext();
            }}
          >
            <span className="icon has-text-centered is-large">
              <i className="icon-right-open" />
            </span>
          </span>
          <p className="help has-text-white">
            Enter a name for your new session
          </p>
        </div>
      </div>
    );
  }

  renderPath() {
    return (
      <div className="column is-one-fifth">
        <div className="control input-control">
          <input
            type="text"
            className="input bottom-border"
            placeholder="Path"
            required
          />
          <span className="focus-border" />
          <p className="help has-text-white">something something path</p>
        </div>
      </div>
    );
  }

  handleNext() {
    this.setState({
      current_step: this.state.current_step + 1
    });
  }

  render() {
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
          {this.state.steps[this.state.current_step].content}
        </div>
        <Steps steps={this.state.steps} current={this.state.current_step} />
      </div>
    );
  }
}

export default CreateFrame;
