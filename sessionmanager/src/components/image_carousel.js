import React, { Component } from 'react';
import Transition from 'react-transition-group/Transition';

const ImageSlide = ({ url, opacity }) => {
  const image_url = `linear-gradient(rgba(26, 31, 35, 0.6), rgba(26, 31, 35, 0.6)), url(${url})`;
  return (
    <div
      className="image-slide"
      style={{ background: image_url, opacity: opacity }}
    />
  );
};

class Carousel extends Component {
  constructor(props) {
    super(props);
    this.state = {
      currentImageIndex: 0,
      isActive: null
    };
  }

  nextSlide(next) {
    console.log('Image Exited, calling next');
    const count = this.props.images.length - 1;
    let index = next > count ? 0 : next;
    console.log('New Index: ', index);
    this.setState({
      currentImageIndex: index,
      isActive: true
    });
  }

  onEntered() {
    setTimeout(
      function() {
        this.setState({
          currentImageIndex: this.state.currentImageIndex,
          isActive: false
        });
        console.log('Is Active Changed');
      }.bind(this),
      4000
    );
  }

  render() {
    return (
      <div className="image-carousel">
        <div className="is-carousel-content">{this.props.content}</div>
        <Transition
          in={this.state.isActive === null ? true : this.state.isActive}
          onEnter={() => this.onEntered()}
          onExited={() => this.nextSlide(this.state.currentImageIndex + 1)}
          timeout={2250}
        >
          {state => {
            switch (state) {
              case 'entering':
                return (
                  <ImageSlide
                    url={this.props.images[this.state.currentImageIndex]}
                    opacity={'1'}
                  />
                );
              case 'entered':
                if (this.state.isActive === null) {
                  this.onEntered();
                }
                return (
                  <ImageSlide
                    url={this.props.images[this.state.currentImageIndex]}
                    opacity={'1'}
                  />
                );
              case 'exiting':
                return (
                  <ImageSlide
                    url={this.props.images[this.state.currentImageIndex]}
                    opacity={'0'}
                  />
                );
              case 'exited':
                return (
                  <ImageSlide
                    url={this.props.images[this.state.currentImageIndex]}
                    opacity={'0'}
                  />
                );
            }
          }}
        </Transition>
      </div>
    );
  }
}

export default Carousel;
