import React, {Component} from "react";
import NavBar from "./../NavBar.jsx";
import {Button} from "react-bootstrap";
import { withRouter } from "react-router-dom";
import "./../css/ConfirmationPage.css"


var site  = 'http://maxjou.se:8000';
class ConfirmationPage extends Component {
    constructor(props){
        super(props);
        this.state ={
            email:""
        }
        this.handleClick = this.handleClick.bind(this)
    }

  
    componentDidMount(){
        fetch(site + '/api/settings/user/',{
          credentials:'include'
        }).then(response => {
          return response.json()}).then(result =>{
            this.setState({email: result[0].targetMail})
          })
      }
    handleClick(e){
        this.props.history.push('/inputs')
    }
    render (){
        return <div className="ConfirmationPage">
            <h1>Skickad!</h1>
            <NavBar/>
            <p>Fakturan är skickad till:<strong>{this.state.email}</strong> </p>
            <Button onClick={this.handleClick} className="knapp">
                Tillbaka
                </Button>
        </div>
    }
}


export default withRouter(ConfirmationPage);