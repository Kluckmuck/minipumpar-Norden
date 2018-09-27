import React, { Component } from "react";
import { Button, FormGroup, FormControl, ControlLabel } from "react-bootstrap";
import { withRouter } from "react-router-dom";
import "./../css/Login.css";

let header = new Headers({
  "Content-Type": "application/json; charset=utf-8",
  "Access-Control-Request-Headers": "*",
  "Access-Control-Allow-Methods": "GET, POST, HEAD, OPTIONS, PUT, DELETE, PATCH",
});
var site  = 'http://maxjou.se:8000';

 class Login extends Component{
  constructor(props) {
    super(props);

    this.state = {
      username: "",
      password: ""
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
      credentials: 'include',
      header:header,
      body: JSON.stringify({
        username: this.state.username,
        password: this.state.password
      })
    }).then(response => {
      if(response.status === 200){
      this.props.history.push('/inputs')
    }else if (response.status === 401){
        alert("Ogiltligt användarnamn och/eller lösenord");
      }
    })
  }
  render() {
    return (
      <div className="Login">
        {/* <h1>Login</h1> */}
          <form onSubmit={this.handleSubmit}>
            <FormGroup controlId="username" bsSize="large">
              <ControlLabel>Email</ControlLabel>
              <FormControl
                autoFocus
                type="text"
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
