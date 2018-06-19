import React, { Component } from "react";
import { Button, FormGroup, FormControl, ControlLabel } from "react-bootstrap";
import "./Login.css";

var siteURL = 'http://127.0.0.1:8000';
var email = 'max@gmail.com';
export default class Login extends Component{
  constructor(props) {
    super(props);
    
    this.state = {
      email: "test@test.se",
      password: "test123123"
    };
  }

  validateForm () {
    return this.state.email.length > 0 && this.state.password.length > 0;
  }
 
  handleChange(e){
    this.setState({[e.target.id]: e.target.value});
 }

  handleSubmit(event) {
    event.preventDefault();
    console.log(this.state.email)
    if(this.state.email === email){
      console.log("correct")
    }else(
      console.log("false")
    )
    console.log(event.preventDefault);
    fetch(siteURL + '/api/login/' , {
      method:  'post',
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers':'origin, content-type, accept',
        "Access-Control-Allow-Methods": "POST, GET, OPTIONS, DELETE, PUT",

        'Content-Type': 'application/json',
        'Accept': 'application/json',                  
        
    },

      body:JSON.stringify({
        username: this.state.email,
        password: this.state.password
      })
    }).then(response => response.json(),);
  }
  render() {
    return (
  <div className="Login">
    <h1>Login</h1>
      <form onSubmit={this.handleSubmit.bind(this)}>
          <FormGroup controlId="email" bsSize="large">
            <ControlLabel>Email</ControlLabel>
            <FormControl
              autoFocus
              type="email"
              value={this.state.email}
              onChange={this.handleChange.bind(this)}
            />
          </FormGroup>
          <FormGroup controlId="password" bsSize="large">
            <ControlLabel>Password</ControlLabel>
            <FormControl
              value={this.state.password}
              onChange={this.handleChange.bind(this)}
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

