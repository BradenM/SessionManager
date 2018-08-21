import React, { Component } from 'react';

class Input extends Component {
  render() {
    return (
      <div className="control input-control">
        <input
          type="text"
          id={'input_' + this.props.label}
          className={'input ' + this.props.className}
          value={this.props.value}
          onChange={e => this.props.handleChange(e)}
          onClick={e => {
            this.props.handleClick(e);
          }}
          required
        />
        <span className="focus-border" />
        <span className="focus-label">{this.props.label}</span>
        <span
          className="focus-submit"
          onClick={() => this.props.handleSubmit()}
        >
          <span className="icon has-text-centered is-large">
            <i className="icon-right-open" />
          </span>
        </span>
        <p className={'help ' + this.props.errorClass}>{this.props.helpText}</p>
      </div>
    );
  }
}

export default Input;
