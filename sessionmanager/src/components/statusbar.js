import React, { Component } from 'react';
import { Icon } from './elements/icons';
import Anime from 'react-anime';

function StatusItem(props) {
  return (
    <div onClick={props.onClick} className="navbar-item">
      {props.value}
    </div>
  );
}

class StatusMenu extends Component {
  renderButton(value) {
    return (
      <a className="button is-light has-text-dark">
        <span className="icon is-large">
          <i>{value}</i>
        </span>
      </a>
    );
  }
  render() {
    return (
      <div className="navbar-menu is-active">
        <div className="navbar-start" />
        <div className="navbar-end">
          <StatusItem
            value={this.renderButton(Icon('cog', 'lg', 'grey-darker'))}
          />
        </div>
      </div>
    );
  }
}

class StatusBar extends Component {
  handleTitle(title) {
    if (title === 'Session Manager') {
      return <h1 className="title is-4 has-text-weight-light">{title}</h1>;
    } else {
      console.log('Alt title');
      return (
        <Anime opacity={[1, 0]} delay={400}>
          <Anime opacity={[0, 1]} delay={800}>
            <a className="button is-light">
              <span className="icon">
                {Icon('arrow-circle-left', 'lg', 'grey')}
              </span>
            </a>
            <h1 className="title is-4 has-text-weight-light">{title}</h1>
          </Anime>
        </Anime>
      );
    }
  }
  render() {
    return (
      <nav
        className="navbar is-light"
        role="navigation"
        aria-label="main navigation"
      >
        <div className="navbar-brand">
          <div className="navbar-item">
            <div className="is-square has-text-centered">
              <span className="icon has-text-centered is-large">
                <i className="icon-camera" />
              </span>
            </div>
          </div>
          <div className="navbar-item">
            {this.handleTitle(this.props.title)}
          </div>
        </div>
        <StatusMenu />
      </nav>
    );
  }
}

export default StatusBar;
