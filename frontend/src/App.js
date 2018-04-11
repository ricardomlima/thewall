import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class AuthPanel extends Component {
  constructor(props){
    super()
    this.handleAuthentication = this.handleAuthentication.bind(this)
    this.handleLogout = this.handleLogout.bind(this)
  }

  handleAuthentication(e){
    e.preventDefault()
    const data = new FormData(e.target);
    this.props.onAuthenticate(true)
  }

  handleLogout(){
    this.props.logout()
  }

  render(){
    return (
      !this.props.loggedIn ? (
      <form onSubmit={this.handleAuthentication}>
        <label>
          Username
          <input type="text" name="username" id="username"/>
        </label>
        <label>
          Password
          <input type="text" name="username" id="username"/>
        </label>
        <button>Login</button>
        <button>Register</button>
      </form>
      ) : (
        <div>
          <span>Hello User</span>
          <button onClick={this.handleLogout}>logout</button>
        </div>
      )
    )
  }
}

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

  constructor(props){
    super(props);
    this.state = {loggedIn: false};
  }

  updateAuth = (loggedIn) => {
    this.setState({loggedIn:loggedIn})
  }

  logoutUser = () => {
    this.setState({loggedIn:false})
  }

  render() {
    return (
      <div>
        <AuthPanel
            loggedIn={this.state.loggedIn}
            logout={this.logoutUser}
            onAuthenticate={this.updateAuth} />
        <Wall loggedIn={this.state.loggedIn} />
      </div>
    );
  }
}

export default App;
