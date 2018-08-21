import React, { Component } from 'react';
import { fetch_sessions, load_thumbs, get_thumb } from './backend';
import Async from 'react-promise';
import Img from 'react-image';
import fallback_img from 'imgs/bg.jpg';

fetch_sessions().then(val => {
  /* Debug */
  console.log('Session Test: ', val);
});

const images = get_thumb(
  require.context('../imgs/thumb', false, /\.(png|jpe?g|svg)$/)
);

const Tile = props => {
  return (
    <Img
      src={props.thumb}
      decode={false}
      container={children => {
        return (
          <div className="tile is-3 is-parent ">
            <div className="tile has-text-centered is-child hvr-outline-in hvr-grow">
              <div className="card">
                <div className="card-filter" />
                <div className="card-image">
                  <figure className="image">{children}</figure>
                </div>
                <div className="card-content">
                  <h1 className="title is-4 has-text-light">{props.value}</h1>
                </div>
              </div>
            </div>
          </div>
        );
      }}
    />
  );
};

class SessionList extends Component {
  constructor(props) {
    super(props);
  }

  loadTiles() {
    return (
      <Async
        promise={load_thumbs()}
        then={() => {
          return this.renderTiles();
        }}
      />
    );
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
      <div className={'session-list'}>
        <div className="tile is-ancestor is-flex is-wrapping">
          {this.loadTiles()}
        </div>
      </div>
    );
  }
}

export default SessionList;
