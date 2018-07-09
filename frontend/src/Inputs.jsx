import React from "react";
import { Button, FormGroup, FormControl, ControlLabel } from "react-bootstrap";
import App from './NavBar.jsx'
import "./Inputs.css"


var site  = 'http://maxjou.se:8000'
class Input extends React.Component {
  constructor(props){
    super(props);
    this.state ={
      name: "",
      adress:"",
      kontakt:"123",
      pumpMng:"",
      datum:"",
      littNr: "",
      resTid:"",
      grundavgift:"",
      pumpStart:"",
      pumpSlut:"",
    }
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  // validateForm() {
  //   return ;
  // }
  handleChange(e){
    this.setState({[e.target.id]: e.target.value});
 }

  handleSubmit (event){
    event.preventDefault();

    fetch (site + '/api/bokning/', {
      method: 'post',
      body: JSON.stringify({
      namn:this.state.name ,
      adress:this.state.adress,
      kontakt:this.state.kontakt,
      pumpMng:this.state.pumpMng,
      datum:this.state.datum,
      littNr:this.state.littNr,
      resTid:this.state.resTid,
      grundavgift:this.state.grundavgift,
      pumpStart:this.state.pumpStart,
      pumpSlut:this.state.pumpSlut,
      })
    }).then(response => {
      console.log(response.status);
    })
  }

  render() {
    return(
    <div className="Inputs">
    <h1>Minipumpar</h1>
    <App/>
      <form onSubmit = {this.handleSubmit}>
        <FormGroup controlId="name" bsSize="large">
          <ControlLabel>Namn:</ControlLabel>
            <FormControl
            type="text"
            value={this.state.name}
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
            type="number"
            value={this.state.kontakt}
            onChange={this.handleChange}
            ></FormControl>
        </FormGroup>
        <FormGroup controlId="pumpMng" bsSize="large">
          <ControlLabel>Pumpmängd:</ControlLabel>
            <FormControl
            type="number"
            value={this.state.pumpMng}
            onChange={this.handleChange}
            ></FormControl>
        </FormGroup>
         <FormGroup controlId="littNr" bsSize="large">
          <ControlLabel>Litermängd:</ControlLabel>
            <FormControl
            type="number"
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
            type="text"
            value={this.state.pumpSlut}
            onChange={this.handleChange}
            ></FormControl>
        </FormGroup>
        <Button
            block
            bsSize="large"
            // disabled={!this.validateForm()}
            type="submit"
          >
            Skicka
          </Button>
      </form>
    </div>);
  }
}

export default  Input;

