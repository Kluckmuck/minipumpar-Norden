import React, { Component } from "react";
import { Button, FormGroup, FormControl, ControlLabel, Modal } from "react-bootstrap";
import { withRouter } from "react-router-dom";
import NavBar from '../NavBar';
import "./../css/Inputs.css";

var site  = 'http://maxjou.se:8000';
class Input extends Component {
  constructor(props){
    super(props);
    this.state ={
      namn:"",
      adress:"",
      kontakt :"",
      pumpMng: "",
      slangStr:"",
      littNr: "",
      resTid: "",
      grundavgift :"",
      datum : "",
      pumpStart :"",
      pumpSlut:"",
      ovrigInfo:"",
      kundmail:"",
      aktuellEmail:"",
      show:false
    }
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
    this.handleExit = this.handleExit.bind(this);
  }

  // * Get the email adress
  componentDidMount(){
    fetch(site + '/api/settings/user/',{
      credentials:'include'
    }).then(response => {
      if(response.status === 404){
        this.setState({showExit: true})
      }else {
        fetch(site + '/api/settings/user/',{
          credentials:'include'
        }).then(response => {
           return response.json()
         }).then(result =>{
            this.setState({aktuellEmail: result[0].targetMail})
          })
      }
     })
    } 

  handleExit(){
    this.props.history.push('/');
  }

  handleChange(e){
    this.setState({[e.target.id]: e.target.value});
  }

  //* POST to backend.
  handleSubmit (event){
    event.preventDefault();
    fetch (site + '/api/bokning/', {
      method: 'POST',
      credentials: 'include',
      body: JSON.stringify({
        namn:this.state.namn,
        kundmail: this.state.kundmail,
        adress:this.state.adress,
        kontakt:this.state.kontakt,
        pumpMng:this.state.pumpMng,
        slangStr: this.state.slangStr,
        littNr:this.state.littNr,
        resTid:this.state.resTid,
        grundavgift:this.state.grundavgift,
        datum:this.state.datum,
        pumpStart:this.state.pumpStart,
        pumpSlut:this.state.pumpSlut,
        ovrigInfo:this.state.ovrigInfo,
      })
    }).then(response => {
      if(response.status === 201){
        this.props.history.push('/confirmationPage')
      }
      if(response.status === 404){
       this.setState({show:true})
      }
      if(response.status === 400){
        console.log(this.state.pumpMng);
      }
     
    })
  }
  
  render() {
    return(
    <div className="Inputs">
      <br/>
    <NavBar/>
      <form onSubmit = {this.handleSubmit}>
        <FormGroup controlId="namn" bsSize="large">
          <ControlLabel>Kund:</ControlLabel>
            <FormControl
            type="text"
            value={this.state.namn}
            onChange={this.handleChange}
            ></FormControl>
        </FormGroup>
        <FormGroup controlId="kundmail" bsSize="large">
          <ControlLabel>Kundmail:</ControlLabel>
            <FormControl
            type="email"
            value={this.state.kundmail}
            onChange={this.handleChange}
            ></FormControl>
        </FormGroup>
        <FormGroup controlId="adress" bsSize="large">
          <ControlLabel>Adress:</ControlLabel>
            <FormControl
            type="text"
            value={this.state.adress}
            onChange={this.handleChange}
            ></FormControl>
        </FormGroup>
        <FormGroup controlId="kontakt" bsSize="large">
          <ControlLabel>Kontakt:</ControlLabel>
            <FormControl
            type="text"
            value={this.state.kontakt}
            onChange={this.handleChange}
            ></FormControl>
        </FormGroup>
        <br/>
        <br/>
        <FormGroup controlId="pumpMng" bsSize="large">
          <ControlLabel>Pumpmängd:</ControlLabel>
            <FormControl
            type="number"
            step="0.1"
            value={this.state.pumpMng}
            onChange={this.handleChange}
            ></FormControl>
        </FormGroup>
        <FormGroup controlId="slangStr" bsSize="large">
          <ControlLabel>Slanglängd:</ControlLabel>
            <FormControl
            type="number"
            value={this.state.slangStr}
            onChange={this.handleChange}
            ></FormControl>
        </FormGroup>
         <FormGroup controlId="littNr" bsSize="large">
          <ControlLabel>Littranummer:</ControlLabel>
            <FormControl
            type="text"
            value={this.state.littNr}
            onChange={this.handleChange}
            ></FormControl>
        </FormGroup>
        <FormGroup controlId="resTid" bsSize="large">
          <ControlLabel>Restid:</ControlLabel>
            <FormControl
            type="number"
            value={this.state.resTid}
            onChange={this.handleChange}
            ></FormControl>
        </FormGroup>
        <FormGroup controlId="grundavgift" bsSize="large">
          <ControlLabel>Grundavgift:</ControlLabel>
            <FormControl
            type="number"
            value={this.state.grundavgift}
            onChange={this.handleChange}
            ></FormControl>
        </FormGroup>
        <br/>
        <br/>
        <FormGroup controlId="datum" bsSize="large">
          <ControlLabel>Datum:</ControlLabel>
            <FormControl
            type="date"
            value={this.state.datum}
            onChange={this.handleChange}
            ></FormControl>
        </FormGroup>
        <FormGroup controlId="pumpStart" bsSize="large">
          <ControlLabel>Pump Start:</ControlLabel>
            <FormControl
            type="time"
            value={this.state.pumpStart}
            onChange={this.handleChange}
            ></FormControl>
        </FormGroup>
        <FormGroup controlId="pumpSlut" bsSize="large">
          <ControlLabel>Pump Slut:</ControlLabel>
            <FormControl
            type="time"
            value={this.state.pumpSlut}
            onChange={this.handleChange}
            ></FormControl>
        </FormGroup>
        <FormGroup controlId="ovrigInfo" bsSize="large">
          <ControlLabel>Övrigt:</ControlLabel>
            <FormControl
            componentClass="textarea"
            value={this.state.ovrigInfo}
            onChange={this.handleChange}
            ></FormControl>
        </FormGroup>
        <br/>
        <ul>
          <li>Följesedeln skickas till: <strong>{this.state.aktuellEmail}</strong></li>
          <li>Kopia skickas till: <strong>{this.state.kundmail}</strong></li>
        </ul>
        <br/>
        <Button
            block
            bsSize="large"
            type="submit"
            >
            Skicka
          </Button>
      </form>
      <br/>
      {/* IF NOT LOGGED IN */}
      <Modal
        show= {this.state.show}
        onHide={this.handleClose}
        container={this}
        aria-labelledby="modal-container"
        className="modal-container"
        >
          <Modal.Header closeButton>
            <Modal.Title id="modal-container">
              Ej inloggad
            </Modal.Title>
          </Modal.Header>
          <Modal.Body>
           Du måste logga in för att skicka fakturor.
          </Modal.Body>
          <Modal.Footer>
            <Button onClick={this.handleExit}>Logga in</Button>
          </Modal.Footer>
        </Modal>

    </div>);
  }
}

export default withRouter(Input);
