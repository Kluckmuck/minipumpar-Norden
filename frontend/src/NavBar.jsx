
import React, {Component }from "react";
import { Link } from "react-router-dom";
import {  Navbar } from "react-bootstrap";
import "./NavBar.css";
 class NavBar extends Component {
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

export default NavBar;