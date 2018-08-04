import React, { Component } from 'react';
// // Font Awesome
// import { library } from '@fortawesome/fontawesome-svg-core';
// import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
// import { faCog } from '@fortawesome/free-solid-svg-icons';
// library.add(faCog);
// My Imports
import StatusBar from './components/statusbar';
import NavBar from './components/navbar';

class App extends Component {
  render() {
    return (
      <div>
        <StatusBar />
        <div className="columns is-gapless">
          <div className="column is-1">
            <NavBar />
          </div>
          <div className="column">
            <h1>Hello</h1>
          </div>
          
        </div>
      </div>
    );
  }
}

export default App;
