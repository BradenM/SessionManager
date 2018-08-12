import React, { Component } from 'react';

class CreateSession extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div>
        <h1 className="title-has-text-white">New Session</h1>
        <button onClick={this.props.toggleCreate}>Close</button>
      </div>
    );
  }
}

export default CreateSession;
