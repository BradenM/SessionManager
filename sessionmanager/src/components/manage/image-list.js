import React, { Component } from 'react';
import Async from 'react-promise';
import { get_thumb } from 'components/backend';
import Img from 'react-image';
import testImage from 'imgs/bg.jpg';

const images = get_thumb(
  require.context('imgs/thumb', false, /\.(png|jpe?g|svg)$/)
);

class ImageList extends Component {
  constructor(props) {
    super(props);
  }

  //   renderImages(){

  //   }

  render() {
    return (
      <section className="grid is-4">
        <figure className="image">
          <Img src={[testImage]} />
        </figure>
        <figure className="image">
          <Img src={['file://' + this.props.session.images[0]]} />
        </figure>
      </section>
    );
  }
}

export default ImageList;
