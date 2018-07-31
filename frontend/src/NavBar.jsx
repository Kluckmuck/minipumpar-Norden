
import React, {Component }from "react";
import { Link } from "react-router-dom";
import {  Navbar , Nav, NavItem} from "react-bootstrap";
import "./NavBar.css";


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
           <Nav className="nav navbar-nav navbar-right navbar-center">
           <NavItem title="Inställningar" componentClass="span" >
             <Link to="/settings"> Inställningar</Link>
           </NavItem>
          </Nav>
         </Navbar.Collapse>
       </Navbar>
     </div>
    }
}
export default NavBar;
