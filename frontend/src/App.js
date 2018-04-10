import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class Post extends Component {
  render(){
    return (
      <div className="Post">
        <div className="Author">
          Ricardo M. Lima
        </div>
        <div className="Message">
          Another brick in the wall
        </div>
      </div>
    )
  }
}

class Wall extends Component {
  render(){
    return (
      <div className="Wall">
        <Post />
        <Post />
        <Post />
        <Post />
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
