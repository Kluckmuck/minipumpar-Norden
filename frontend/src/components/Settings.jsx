import React, {Component} from "react";
import "./Settings.css"
import { FormControl, ControlLabel, FormGroup, Button } from "react-bootstrap";
import NavBar from "../NavBar.jsx";

class Settings extends Component{
  constructor(props) {
    super(props);

    this.state = {
      email:""
    }
    this.handleChange = this.handleChange.bind(this)
  }

  validateForm(){
    return this.state.email.length > 0 ;
  }

  handleChange(e){
    this.setState({[e.target.id]: e.target.value});
  }
  handleSubmit(e){

    e.preventDefault();

    console.log()
  }


  render(){
    return(<div className="Settings">
      <h1>Inställningar</h1>
      <NavBar/>
      <p>Här kan du skriva in den mail som fakturan skall skickas.</p>
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
        >Ändra
        </Button>


      </form>
    </div>

    )
  }
} 

export default Settings;