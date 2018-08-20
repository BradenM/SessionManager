import React, { Component } from 'react';
import Input from '../elements/input';
import CircleProgress from '../elements/progress';

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
        onComplete={() => this.props.handleSubmit()}
      />
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
