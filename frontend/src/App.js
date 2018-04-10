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

  state = {
    posts: [
      {"author":"Ricardo Monteiro e Lima", "message":"one brick in the Wall"},
      {"author":"Rafael Monteiro e Lima",  "message":"two bricks in the Wall"},
      {"author":"Larissa Espindola",       "message":"three bricks in the Wall"},
      {"author":"Larissa Capelari",        "message":"four bricks in the Wall"},
    ]
  }

  render(){
    return (
      <div className="Wall">
        {this.state.posts.map(post => (
          <Post author={post.author} message={post.message} />
        ))}
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
