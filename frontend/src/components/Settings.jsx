import React, {Component} from "react";
import "./css/Settings.css"
import { FormControl, ControlLabel, FormGroup, Button, Modal } from "react-bootstrap";
import NavBar from "./NavBar.jsx";

var date =  new Date().now;
var site  = 'http://maxjou.se:8000';
class Settings extends Component{
  constructor(props) {
    super(props);

    this.state = {
      email:"",
      show:false
    }
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleClose = this.handleClose.bind(this);
  }

  componentDidMount(){
    fetch(site + '/api/settings/user/',{
      credentials:'include'
    }).then(response => { 
      return response.json()}).then(result =>{
        this.setState({email: result[0].targetMail})
      })
  }

  validateForm(){
    return this.state.email.length > 0 && this.state.email.includes("@");
  }

  handleChange(e){
    this.setState({[e.target.id]: e.target.value});
  }
  handleSubmit(e){
    e.preventDefault();
    fetch (site + '/api/settings/targetMail/',{
      method: 'post',
      credentials:'include',
      body: JSON.stringify({
        email: this.state.email
      })
    })
  }
  
  handleClose(){
    this.setState({show: false})
  }


  render(){
    return(<div className="Settings">
      <br/>
      <NavBar/>
      <p>Här kan du skriva in den mail som fakturan skall skickas till.</p>
      <p>Just nu skickas fakturan till: <strong>{this.state.email}</strong></p>
      <form onSubmit={this.handleSubmit}>
        <FormGroup controlId="email" bsSize="large">
          <ControlLabel>Email </ControlLabel>
          <FormControl
          autoFocus
          type="email"
          value={this.state.email}
          onChange={this.handleChange}></FormControl>
        </FormGroup>
        <Button
        block
        bsSize="large"
        disabled={!this.validateForm()}
        type="submit"
        onClick= {()=> this.setState({ show: true })}
        >Ändra
        </Button>

        <Modal
        show= {this.state.show}
        onHide={this.handleClose}
        container={this}
        disabled={!this.validateForm()}
        aria-labelledby="modal-container"
        className="modal-container"
        >
          <Modal.Header closeButton>
            <Modal.Title id="modal-container">
              Bekräftad
            </Modal.Title>
          </Modal.Header>
          <Modal.Body>
            Eposten är ändrad. 
          </Modal.Body>
          <Modal.Footer>
            <Button onClick={this.handleClose}>Stäng</Button>
          </Modal.Footer>
        </Modal>

      </form>
    </div>

    )
  }
} 

export default Settings;