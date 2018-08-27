import React, { Component } from 'react';
import Async from 'react-promise';
import { get_imgs } from 'components/backend';
import Img from 'react-image';
import Anime from 'react-anime';
import TextFit from 'react-textfit';

class ImageList extends Component {
  constructor(props) {
    super(props);
  }

  shouldComponentUpdate(nextProps, nextState) {
    return false;
  }

  renderImages(images) {
    return (
      <Async
        promise={get_imgs(images)}
        then={base_imgs => {
          let renders = [];
          base_imgs.forEach((img, i) => {
            renders.push(
              <Anime
                opacity={[0, 1]}
                translateY={[-16, 0]}
                duration={1000}
                delay={i * 150}
              >
                <figure
                  key={i}
                  onMouseEnter={() => this.props.onHover(img)}
                  className="image is-session-img is-unselectable"
                >
                  <Img
                    draggable="false"
                    src={['data:image/jpeg;base64,' + img.thumb]}
                  />
                  <span className="img-caption">
                    <TextFit mode="single">{img.display_name}</TextFit>
                  </span>
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
