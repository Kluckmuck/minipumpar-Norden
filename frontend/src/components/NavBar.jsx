
import React, {Component }from "react";
import { Link } from "react-router-dom";
import {  Navbar , Nav, NavItem,} from "react-bootstrap";
import "./NavBar.css";

 class NavBar extends Component {
   render (){
   return  <div className="container">
       <Navbar fluid collapseOnSelect>
         <Navbar.Header>
           <Navbar.Brand>
             <Link to="/inputs">Formulär</Link>
           </Navbar.Brand>
           <Navbar.Toggle />
         </Navbar.Header>
           <Nav>
            <NavItem pullRight>
            <Link to="/settings"> Inställningar </Link>  
            </NavItem>
          </Nav>
       </Navbar>
     </div>
    }
}
export default NavBar;

