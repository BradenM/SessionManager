import React, { Component } from 'react';
import { fetchHello } from './backend';
import Async from 'react-promise';

const Tile = props => {
  return (
    <div className="tile is-3 is-parent">
      <div className="tile has-text-centered is-child">
        <div className="card">
          <div className="card-image" />
          <div className="card-content">
            <h1 className="title is-4">{props.value}</h1>
          </div>
        </div>
      </div>
    </div>
  );
};

class SessionList extends Component {
  constructor(props) {
    super(props);
  }
  renderTest() {
    return <Async promise={fetchHello()} then={val => val} />;
  }
  render() {
    return (
      <div className="session-list">
        <div className="tile is-ancestor">
          <Tile value={this.renderTest()} />
        </div>
      </div>
    );
  }
}

export default SessionList;
