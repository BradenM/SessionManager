import React, { Component } from 'react';
import { fetch_sessions, get_thumb } from './backend';
import Async from 'react-promise';

fetch_sessions().then(val => {
  /* Debug */
  console.log('Session Test: ', val);
});

const images = get_thumb(
  require.context('../imgs/thumb', false, /\.(png|jpe?g|svg)$/)
);

const Tile = props => {
  return (
    <div className="tile is-3 is-parent ">
      <div className="tile has-text-centered is-child hvr-outline-in hvr-grow">
        <div className="card">
          <div className="card-filter" />
          <div className="card-image">
            <figure className="image">
              <img src={props.thumb} alt="" />
            </figure>
          </div>
          <div className="card-content">
            <h1 className="title is-4 has-text-light">{props.value}</h1>
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

  renderTiles() {
    return (
      <Async
        promise={fetch_sessions()}
        then={sessions => {
          let tiles = [];
          sessions.forEach(s => {
            tiles.push(<Tile value={s.name} thumb={images[s.cover_img]} />);
          });
          return tiles;
        }}
      />
    );
  }
  render() {
    return (
      <div className="session-list">
        <div className="tile is-ancestor is-flex is-wrapping">
          {this.renderTiles()}
        </div>
      </div>
    );
  }
}

export default SessionList;
