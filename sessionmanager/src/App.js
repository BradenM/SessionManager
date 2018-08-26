import React, { Component } from 'react';
import StatusBar from './components/statusbar';
import NavBar from './components/navbar';
import Carousel from './components/image_carousel';
import SessionList from 'components/sessions/list';
import SessionInfo from 'components/sessions/info';
import ImageList from 'components/manage/image-list';
import CreateFrame from './components/create/create_window';
import image1 from './imgs/bg.jpg';
import image2 from './imgs/ol.jpg';

class MainWindow extends Component {
  constructor(props) {
    super(props);
    this.state = {
      active_session: null
    };

    this.handleSessionHover = this.handleSessionHover.bind(this);
  }

  handleSessionHover(session) {
    if (session === this.state.active_session) {
      return;
    }
    this.setState({
      active_session: session
    });
  }

  render() {
    let active = this.props.active ? '' : this.props.foreground;
    return (
      <div className={'window main-window ' + active}>
        <StatusBar title={this.props.title} />
        <div className="columns is-gapless">
          <div className="column is-narrow">
            <NavBar toggleCreate={this.props.toggleCreate} />
          </div>
          <div
            className={
              'column is-3 has-height-full ' +
              (this.props.infoActive ? '' : 'is-hidden')
            }
          >
            <SessionInfo session={this.state.active_session} />
          </div>
          <div
            className={
              'column is-content-window has-height-full ' +
              (this.props.listActive ? '' : 'is-hidden')
            }
          >
            <Carousel
              slideOn={this.props.active}
              images={[image1, image2]}
              slideDelay={2000}
              content={
                <div>
                  <SessionList
                    activeSession={this.state.active_session}
                    onHover={s => this.handleSessionHover(s)}
                    onClick={s => this.props.toggleManage(s)}
                  />
                </div>
              }
            />
          </div>
          <ManageWindow
            active={this.props.openSession !== null}
            session={this.props.openSession}
          />
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

class ManageWindow extends Component {
  render() {
    let active = this.props.active ? 'is-active' : '';
    return (
      <div className={'window manage-window ' + (active ? '' : 'is-hidden')}>
        <div className="image-list">
          {this.props.active ? (
            <ImageList session={this.props.session} />
          ) : (
            undefined
          )}
        </div>
      </div>
    );
  }
}

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      main: {
        active: true,
        foreground: '',
        infoActive: true,
        listActive: true,
        panelContent: null
      },
      create: {
        active: false
      },
      manage: {
        active: false,
        session: null
      }
    };
  }

  handleCreateWindow() {
    this.setState({
      main: {
        active: !this.state.main.active,
        foreground: 'is-blurred',
        infoActive: true,
        listActive: true
      },
      manage: {
        active: false,
        session: null
      },
      create: {
        active: !this.state.create.active
      }
    });
    console.log('Create window toggled');
  }

  handleManageWindow(session) {
    this.setState({
      main: {
        active: !this.state.main.active,
        listActive: false,
        infoActive: false
      },
      manage: {
        active: !this.state.manage.active,
        session: session
      }
    });
  }

  render() {
    let active_session = this.state.manage.session;
    return (
      <div>
        <MainWindow
          active={this.state.main.active}
          foreground={this.state.main.foreground}
          listActive={this.state.main.listActive}
          infoActive={this.state.main.infoActive}
          openSession={this.state.manage.session}
          title={
            active_session !== null ? active_session.name : 'Session Manager'
          }
          toggleManage={s => this.handleManageWindow(s)}
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
