import React, { Component } from 'react';

function NavButton(props) {
    return (
        <a href={props.href} onClick={props.onClick} className="navbar-item">
            {props.value}
        </a>
    )
}

function NavInput(props) {
    return (
        <div className="navbar-item">
            <div className="field has-addons">
                <div className="control">
                    <a className="button is-static">
                        S
                    </a>
                </div>
                <div className="control">
                    <input className="input test-input" type="text" placeholder={props.placeholder} />
                </div>
            </div>
        </div>
    )
}

class NavMenu extends Component {
    render() {
        return (
            <div className='navbar-menu is-active'>
                <div className='navbar-start'>
                    <NavButton value='Create' />
                    <NavButton value='Recent' />
                </div>
                <div className='navbar-end'>
                    <NavInput placeholder='Search' />
                    <NavButton value='Settings' />
                </div>
            </div>
        )
    }
}

class NavBar extends Component {
    render() {
        return (
            <nav className="navbar is-dark has-border bd-bottom" role='navigation' aria-label="main navigation">
                <div className="navbar-brand">
                    <h1 className="navbar-item title is-4">Session Manager</h1>
                </div>
                <NavMenu />
            </nav>
        )
    }
}

export default NavBar;
