import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class AuthPanel extends Component {
  constructor(props){
    super()
    this.state = {email:'', password:''}

    this.handleAuthentication = this.handleAuthentication.bind(this)
    this.handleRegistration = this.handleRegistration.bind(this)
    this.handleLogout = this.handleLogout.bind(this)
    this.handleEmailChange = this.handleEmailChange.bind(this)
    this.handlePasswordChange = this.handlePasswordChange.bind(this)
  }

  handleRegistration(e){
    e.preventDefault()
    const postData = {
      email:this.state.email,
      password1: this.state.password,
      password2: this.state.password,
    }

    fetch('http://localhost/api/v1/auth/registration/', {
      method:'POST',
      body:JSON.stringify(postData),
      headers: {'content-type': 'application/json'},
      mode:'cors'
    })
    .then((res) => {
      if(res.ok){
        this.props.onAuthenticate(true)
      }
    })
  }

  handleAuthentication(e){
    e.preventDefault()
    const postData = {
      email:this.state.email,
      password: this.state.password,
    }

    fetch('http://localhost/api/v1/auth/login/', {
      method:'POST',
      body:JSON.stringify(postData),
      headers: {'content-type': 'application/json'},
      mode:'cors'
    })
    .then((res) => {
      if(res.ok){
        this.props.onAuthenticate(true)
      }
    })
  }

  handleLogout(){
    this.props.logout()
  }

  handleEmailChange(e){
    this.setState({email: e.target.value})
  }

  handlePasswordChange(e){
    this.setState({password: e.target.value})
  }

  render(){
    return (
      !this.props.loggedIn ? (
      <form>
        <label>
          Username
          <input onChange={this.handleEmailChange} type="text" name="email" id="email"/>
        </label>
        <label>
          Password
          <input onChange={this.handlePasswordChange} type="password" name="password" id="password"/>
        </label>
        <button onClick={this.handleAuthentication}>Login</button>
        <button onClick={this.handleRegistration}>Register</button>
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

class PostForm extends Component {

  render() {
    return (
      <form id='PostForm'>
        <textarea className="PostForm"></textarea>
        <button>Post to the Wall</button>
      </form>
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
        <PostForm />
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
