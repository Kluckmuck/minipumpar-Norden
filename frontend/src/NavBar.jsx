
import React, {Component }from "react";
import { Link } from "react-router-dom";
import {  Navbar , NavItem, Nav, NavDropdown, MenuItemLink, MenuItem} from "react-bootstrap";
import "./NavBar.css";

var FontAwesome = require('react-fontawesome');
 class NavBar extends Component {
   render (){
   return  <div className="container">
       <Navbar fluid collapseOnSelect>
         <Navbar.Header>
           <Navbar.Brand>
             <Link to="/inputs">Minipumpar</Link>
           </Navbar.Brand>
           <Navbar.Toggle />
         </Navbar.Header>
         <Navbar.Collapse>
           <Nav>
           <NavDropdown title="Inställningar" >
           
             <Link to="/"> <MenuItem>Settings</MenuItem></Link>
           </NavDropdown>
          </Nav>
         </Navbar.Collapse>
       </Navbar>
     </div>
    }
}
export default NavBar;

