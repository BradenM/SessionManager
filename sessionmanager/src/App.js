import React, { Component } from 'react';
import StatusBar from './components/statusbar';
import NavBar from './components/navbar';
import Carousel from './components/image_carousel';
import SessionList from './components/sessions';
import image1 from './imgs/bg.jpg';
import image2 from './imgs/ol.jpg';

class App extends Component {
  render() {
    return (
      <div>
        <StatusBar />
        <div className="columns is-gapless">
          <div className="column is-narrow">
            <NavBar />
          </div>
          <div className="column is-3 has-height-full">
            <h1>Hello</h1>
          </div>
          <div className="column is-content-window has-height-full">
            <Carousel
              images={[image1, image2]}
              slideDelay={2000}
              content={
                <div>
                  <SessionList />
                </div>
              }
            />
          </div>
        </div>
      </div>
    );
  }
}

export default App;
