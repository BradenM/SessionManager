import React, { Component } from 'react';
import { Icon } from './elements/icons';

class NavMenu extends Component {
  renderButton(onClick, icon, size, color) {
    return (
      <li>
        <a href="#" className="button is-dark" onClick={onClick}>
          <span className="icon is-large">
            <i>{Icon(icon, size, color)}</i>
          </span>
        </a>
      </li>
    );
  }

  render() {
    return (
      <div>
        {this.renderButton(null, 'th', 'lg')}
        {this.renderButton(this.props.toggleCreate, 'plus', 'lg')}
      </div>
    );
  }
}

class NavBar extends Component {
  render() {
    return (
      <aside id="nav_menu" className="menu has-background-dark">
        <ul className="menu-list">
          <NavMenu toggleCreate={this.props.toggleCreate} />
        </ul>
      </aside>
    );
  }
}

export default NavBar;
