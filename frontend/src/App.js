import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class Post extends Component {
  render(){
    return (
      <div className="Post">
        <h2 className="Author">
          {this.props.author}
        </h2>
        <div className="Message">
          {this.props.message}
        </div>
      </div>
    )
  }
}

class Wall extends Component {
  render(){
    return (
      <div className="Wall">
        <Post author="Ricardo Monteiro e Lima" message="one brick in the wall"/>
        <Post author="Rafael Monteiro e Lima"  message="two bricks in the wall"/>
        <Post author="Larissa Espindola"       message="three brick in the wall"/>
        <Post author="Larissa Capelari"        message="four bricks in the wall"/>
      </div>
    )
  }
}

class App extends Component {
  render() {
    return (
      <Wall />
    );
  }
}

export default App;
