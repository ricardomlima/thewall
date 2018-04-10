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

  constructor(props) {
    super(props)
    this.state = {
      error: null,
      isLoaded: false,
      posts: []
    }
  }

  componentDidMount(){
      fetch('http://localhost/api/v1/posts')
      .then(res => res.json())
      .then((result) => {

        // Populating state with posts from backend
        // server
        this.setState({
          isLoaded: true,
          posts: result.results
        },
        (error) => {
          this.setState({
            isLoaded: true,
            error
          })
        })

      })
  }

  render(){
    return (
      <div className="Wall">
        {this.state.posts.map(post => (
          <Post key={post.id} author={post.author} message={post.message} />
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
