import React, { Component } from "react";
import { Button, FormGroup, FormControl, ControlLabel, Modal } from "react-bootstrap";
import { withRouter } from "react-router-dom";

import "./Login.css";

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
      username: "test@test.se",
      password: "test123123",
      showExit:false
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleClose = this.handleClose.bind(this);
  }

  validateForm () {
    return this.state.username.length > 0 && this.state.password.length > 0;
  }

  handleChange(e){
    this.setState({[e.target.id]: e.target.value});
 }
 handleClose(){
  this.setState({showExit: false})
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
      this.setState({showExit: true})
      console.log(this.state.showExit)
      }
    })
  }
  render() {
    return (<div className="Login">
        {/* <h1>Login</h1> */}
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
          <Modal
              show= {this.state.showExit}
              onHide={this.handleClose}
              container={this}
              aria-labelledby="modal-container"
              className="modal-container"
              >
              <Modal.Header closeButton>
                <Modal.Title id="modal-container">
                  Felaktigt användarnamn/lösenord
                </Modal.Title>
              </Modal.Header>
              <Modal.Body>
                Du har angivit ett felaktigt användarnamn eller lösenord. 
              </Modal.Body>
              <Modal.Footer>
                <Button onClick={this.handleClose}> Stäng</Button>
              </Modal.Footer>
        </Modal>
      </div>
  );
}

}

export default withRouter(Login);
