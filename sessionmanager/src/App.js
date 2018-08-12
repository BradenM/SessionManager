import React, { Component } from 'react';
import StatusBar from './components/statusbar';
import NavBar from './components/navbar';
import Carousel from './components/image_carousel';
import SessionList from './components/sessions';
import CreateFrame from './components/create/create_window';
import image1 from './imgs/bg.jpg';
import image2 from './imgs/ol.jpg';

class MainWindow extends Component {
  render() {
    let active = this.props.active ? '' : 'is-blurred';
    return (
      <div className={'window main-window ' + active}>
        <StatusBar />
        <div className="columns is-gapless">
          <div className="column is-narrow">
            <NavBar toggleCreate={this.props.toggleCreate} />
          </div>
          <div className="column is-3 has-height-full">
            <h1>Hello</h1>
          </div>
          <div className="column is-content-window has-height-full">
            <Carousel
              slideOn={this.props.active}
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

class CreateWindow extends Component {
  render() {
    let active = this.props.active ? 'is-active' : '';
    return (
      <div className={'window create-window overlay ' + active}>
        <CreateFrame toggleCreate={this.props.toggleCreate} />
      </div>
    );
  }
}

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      main: {
        active: true
      },
      create: {
        active: false
      }
    };
  }

  handleCreateWindow() {
    this.setState({
      main: {
        active: !this.state.main.active
      },
      create: {
        active: !this.state.create.active
      }
    });
    console.log('Create window toggled');
  }

  render() {
    return (
      <div>
        <MainWindow
          active={this.state.main.active}
          toggleCreate={() => {
            this.handleCreateWindow();
          }}
        />
        <CreateWindow
          active={this.state.create.active}
          toggleCreate={() => {
            this.handleCreateWindow();
          }}
        />
      </div>
    );
  }
}

export default App;
