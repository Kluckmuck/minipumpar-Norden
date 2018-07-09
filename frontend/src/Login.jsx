import React, { Component } from "react";
import { Button, FormGroup, FormControl, ControlLabel } from "react-bootstrap";
import "./Login.css";
import { withRouter } from "react-router-dom";

var site  = 'http://maxjou.se:8000';

 class Login extends Component{
  constructor(props) {
    super(props);
    
    this.state = {
      username: "test@test.se",
      password: "test123123"
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }


  validateForm () {
    return this.state.username.length > 0 && this.state.password.length > 0;
  }
 
  handleChange(e){
    this.setState({[e.target.id]: e.target.value});
 }

  handleSubmit(event) {
    event.preventDefault();

    fetch (site + '/api/login/', {
      method: 'post',
      body: JSON.stringify({
        username: this.state.username,
        password: this.state.password
      })
    }).then(response => {
      console.log(response.status)
      if(response.status === 200){
      console.log("Login successfull");
      this.props.history.push('/inputs')
      }else if (response.status === 204){
        console.log("Username passwod do not match");
      }else {
        console.log("username does not exist")
        alert("username does not exist");
      }
      })

    console.log('Hello')
  }
  render() {
    return (
  <div className="Login">
    <h1>Login</h1>
      <form onSubmit={this.handleSubmit}>
          <FormGroup controlId="username" bsSize="large">
            <ControlLabel>Email</ControlLabel>
            <FormControl
              autoFocus
              type="email"
              value={this.state.username}
              onChange={this.handleChange}
            />
          </FormGroup>
          <FormGroup controlId="password" bsSize="large">
            <ControlLabel>Password</ControlLabel>
            <FormControl
              value={this.state.password}
              onChange={this.handleChange}
              type="password"
            />
          </FormGroup>
          <Button
            block
            bsSize="large"
            disabled={!this.validateForm()}
            type="submit"
          >
            Login
          </Button>
      </form>
  </div>
  );
}

}

export default withRouter(Login);



