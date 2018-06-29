
import React, {Component }from "react";
import { Link } from "react-router-dom";
import {  Navbar } from "react-bootstrap";
import "./css/App.css";
 class App extends Component {
    render (){
        return  <div className="container">
       <Navbar fluid collapseOnSelect>
         <Navbar.Header>
           <Navbar.Brand>
             <Link to="/">NavBar</Link>
           </Navbar.Brand>
           <Navbar.Toggle />
         </Navbar.Header>
       </Navbar>
     </div>
    }
}

export default App;