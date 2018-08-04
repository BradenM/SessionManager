import React, { Component } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

class NavMenu extends Component {
  renderIconButton(icon) {
    return (
      <span className="icon is-large">
        <i>{icon}</i>
      </span>
    );
  }

  render() {
    return (
      <div>
        <li>
          <a className="button is-dark">
            <span className="icon is-large">
              <i>
                <FontAwesomeIcon size="lg" icon="cog" aria-hidden="true" />
              </i>
            </span>
          </a>
        </li>
        <li>
          <a className="button is-dark">
            <span className="icon is-large">
              <i>
                <FontAwesomeIcon size="lg" icon="cog" aria-hidden="true" />
              </i>
            </span>
          </a>
        </li>
        <li>
          <a className="button is-dark">
            <span className="icon is-large">
              <i>
                <FontAwesomeIcon size="lg" icon="cog" aria-hidden="true" />
              </i>
            </span>
          </a>
        </li>
      </div>
    );
  }
}

class NavBar extends Component {
  render() {
    return (
      <aside id='nav_menu' className="menu has-background-dark">
        <ul className="menu-list">
          <NavMenu />
        </ul>
      </aside>
    );
  }
}

export default NavBar;
