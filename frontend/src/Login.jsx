import React, { Component } from "react";
import { Button, FormGroup, FormControl, ControlLabel } from "react-bootstrap";
import "./Login.css";
import { withRouter } from "react-router-dom";

var site  = 'http://maxjou.se:8000';

 class Login extends Component{
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


    fetch (site + '/api/login/', {
      credentials: 'include',
      method: 'post',
      body: JSON.stringify({
        username: this.state.email,
        password: this.state.password
      })
    }).then(response => {
      response.json().then(data => ({
        data: data,
        status: response.status
      })
    ).then(res =>{
      console.log(res.status, res.data.title)
    })
  })

    event.preventDefault();
    this.props.history.push('/inputs')
    console.log('Hello')
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

export default withRouter(Login);
