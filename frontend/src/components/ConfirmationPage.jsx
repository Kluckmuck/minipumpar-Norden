import React, {Component} from "react";
import NavBar from "./NavBar.jsx";
import {Button} from "react-bootstrap";
import { withRouter } from "react-router-dom";
import "./css/ConfirmationPage.css"


//TODO:Check if works
class ConfirmationPage extends Component {
    constructor(props){
        super(props);
        this.handleClick = this.handleClick.bind(this)
    }
    handleClick(e){
        this.props.history.push('/inputs')
    }
    render (){
        return <div className="ConfirmationPage">
            <h1>Skickad!</h1>
            <NavBar/>
            <p>Fakturan är skickad till: </p>
            <Button onClick={this.handleClick} className="knapp">
                Tillbaka
                </Button>
        </div>
    }
}


export default withRouter(ConfirmationPage);