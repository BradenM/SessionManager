import React, { Component } from 'react';
import Input from '../elements/input';
import CircleProgress from '../elements/progress';

class StepPage extends Component {
  constructor(props) {
    super(props);
    this.renderInput = this.renderInput.bind(this);
    this.renderLoad = this.renderLoad.bind(this);
    this.renderFinish = this.renderFinish.bind(this);
  }

  renderStep(step) {
    const renderTypes = {
      input: this.renderInput,
      load: this.renderLoad,
      finish: this.renderFinish
    };
    let r = renderTypes[step.type];
    return r(step);
  }
  renderInput(step) {
    return (
      <Input
        className="fancy-step"
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
        onComplete={() => this.props.handleSubmit()}
      />
    );
  }

  renderFinish(step) {
    return (
      <div className="pg-checkmark">
        <svg
          className="checkmark"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 52 52"
        >
          <circle
            className="checkmark__circle"
            cx="26"
            cy="26"
            r="25"
            fill="none"
          />
          <path
            className="checkmark__check"
            fill="none"
            d="M14.1 27.2l7.1 7.2 16.7-16.8"
          />
        </svg>
        <h1 className="title is-3">{step.helpText}</h1>
        <a
          onClick={() => this.props.handleSubmit()}
          className="button is-white is-outlined"
        >
          Close
        </a>
      </div>
    );
  }

  render() {
    return (
      <div className="column is-one-fifth">
        {this.renderStep(this.props.step)}
      </div>
    );
  }
}

export default StepPage;
