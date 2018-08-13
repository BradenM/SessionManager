import React, { Component } from 'react';
import { Circle } from 'rc-progress';

class CircleProgress extends Component {
  constructor(props) {
    super(props);
    this.state = {
      style: this.getStyle(this.props.style)
    };
    this.renderColor = this.renderColor.bind(this);
  }

  renderColor() {
    let val = this.props.percent;
    switch (true) {
      case val <= 20:
        return 0;
      case val <= 40:
        return 1;
      case val <= 60:
        return 2;
      case val <= 80:
        return 3;
      case val <= 100:
        return 4;
    }
  }

  getStyle(type) {
    let inner_label = {
      class: 'circle-pg has-inner-label',
      stroke: {
        width: 2,
        color: ['#165b7a', '#1b6d93', '#2492c4', '#28a4dc', '#2db7f5'],
        cap: 'square'
      },
      trail: {
        width: 0.5,
        color: '#ced0d2'
      }
    };
    let types = {
      'inner-label': inner_label
    };
    return types[type];
  }

  render() {
    let style = this.state.style;
    return (
      <div className={style.class}>
        <Circle
          percent={this.props.percent}
          strokeWidth={style.stroke.width}
          trailWidth={style.trail.width}
          trailColor={style.trail.color}
          strokeColor={style.stroke.color[this.renderColor()]}
          strokeLinecap={style.stroke.cap}
        />
        <span className="pg-label has-has-text-weight-semibold">
          <span className="is-1 has-text-light">{this.props.percent}%</span>
          <h3 className="is-2 has-text-white">{this.props.title}</h3>
        </span>
      </div>
    );
  }
}

export default CircleProgress;
