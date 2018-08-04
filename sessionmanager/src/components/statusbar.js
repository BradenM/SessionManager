import React, { Component } from 'react';
import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import {
  faCog,
  faPlus,
  faCameraRetro,
  faCamera
} from '@fortawesome/free-solid-svg-icons';

// Font Awesome
library.add(faCog, faPlus, faCameraRetro, faCamera);

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
      <a className="button is-dark">
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
            value={this.renderButton(
              <FontAwesomeIcon size="lg" icon="cog" aria-hidden="true" />
            )}
          />
        </div>
      </div>
    );
  }
}

class StatusBar extends Component {
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
            <h1 className="title is-4">Session Manager</h1>
          </div>
        </div>
        <StatusMenu />
      </nav>
    );
  }
}

export default StatusBar;
