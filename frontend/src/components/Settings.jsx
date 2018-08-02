import React, {Component} from "react";
import "./css/Settings.css"
import { FormControl, ControlLabel, FormGroup, Button } from "react-bootstrap";
import NavBar from "./NavBar.jsx";


var site  = 'http://maxjou.se:8000';
class Settings extends Component{
  constructor(props) {
    super(props);

    this.state = {
      email:""
    }
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  //TODO: Get method to work
  componentDidMount(){
    console.log("got here");
    fetch(site + '/setttings/user/',{
      method: 'GET',
      credentials: 'include',
    }).then(response => {

      console.log(response.json() + "hej");
    })
  }

  validateForm(){
    return this.state.email.length > 0 ;
  }

  handleChange(e){
    this.setState({[e.target.id]: e.target.value});
  }
  handleSubmit(e){
    console.log("got here")
    e.preventDefault();
    fetch (site + '/api/settings/targetMail/',{
      method: 'post',
      credentials:'include',
      body: JSON.stringify({
        email: this.state.email
      })
    }).then(response => {
      console.log(response.status);
    })
    console.log()
  }



  render(){
    return(<div className="Settings">
      <h1>Inställningar</h1>
      <NavBar/>
      <p>Här kan du skriva in den mail som fakturan skall skickas.</p>
      <p>Just nu skickas fakturan till: </p>
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
        >Ändra
        </Button>


      </form>
    </div>

    )
  }
} 

export default Settings;