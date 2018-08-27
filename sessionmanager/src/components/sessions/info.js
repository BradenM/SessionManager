import React, { Component } from 'react';

class SessionInfo extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    let s = this.props.session;
    let name = s !== null ? s.name : '';
    let date = s !== null ? s.create_date : '';
    return (
      <div className="session-info">
        <h1 className="title">{name}</h1>
        <h6 className="subtitle has-text-grey">{date}</h6>
      </div>
    );
  }
}

export default SessionInfo;
