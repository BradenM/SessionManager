import React, { Component } from 'react';
import { Icon } from './icons';

class NavMenu extends Component {
  renderButton(icon, size, color) {
    return (
      <li>
        <a href="" className="button is-dark">
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
        {this.renderButton('th', 'lg')}
        {this.renderButton('plus', 'lg')}
      </div>
    );
  }
}

class NavBar extends Component {
  render() {
    return (
      <aside id="nav_menu" className="menu has-background-dark">
        <ul className="menu-list">
          <NavMenu />
        </ul>
      </aside>
    );
  }
}

export default NavBar;
