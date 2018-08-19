/*

Create Window Timeline component 

*/

import React, { Component } from 'react';
import { resolve } from 'path';
const path = require('path');

const formatHelp = val => {
  /*
        Format Step Values into Step Details on markers
    */
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

export default StepTimeline;
