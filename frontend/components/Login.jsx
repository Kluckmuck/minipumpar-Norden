import React, { Component } from "react";
import { Button, FormGroup, FormControl, ControlLabel } from "react-bootstrap";
import "./Login.css";

var siteURL = 'http://cities.jonkri.se/';
var email = 'max@gmail.com';
export default class Login extends Component{
  constructor(props) {
    super(props);
    
    this.state = {
      email: "max@gmail.com",
      password: ""
    };
  }

  validateForm() {
    return this.state.email.length > 0 && this.state.password.length > 0;
  }
 
  handleChange (event) {
    this.setState({
      [event.target.id]: event.target.value
    });  
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
    fetch(siteURL , {
      method:  'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      body:JSON.stringify({
        name: this.state.email,
        population: this.state.password
      })
      // .then((response) =>{
      //   console.log(response.json());
      //     return response.json();
      // })
    });
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

