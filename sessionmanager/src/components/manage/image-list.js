import React, { Component } from 'react';
import Async from 'react-promise';
import { get_imgs } from 'components/backend';
import Img from 'react-image';
import Anime from 'react-anime';

class ImageList extends Component {
  constructor(props) {
    super(props);
  }

  renderImages(paths) {
    return (
      <Async
        promise={get_imgs(paths)}
        then={imgs => {
          let renders = [];
          imgs.forEach((img, i) => {
            renders.push(
              <Anime
                opacity={[0, 1]}
                translateY={[-16, 0]}
                duration={1000}
                delay={i * 150}
              >
                <figure key={i} className="image is-unselectable">
                  <Img
                    draggable="false"
                    src={['data:image/jpeg;base64,' + img]}
                  />
                </figure>
              </Anime>
            );
          });
          return renders;
        }}
      />
    );
  }

  render() {
    return (
      <section className="grid is-4">
        {this.renderImages(this.props.session.images)}
      </section>
    );
  }
}

export default ImageList;
