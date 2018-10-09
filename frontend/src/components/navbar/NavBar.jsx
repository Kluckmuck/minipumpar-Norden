import React, {Component }from "react";
import { Navbar, Nav, NavItem} from "react-bootstrap";
import { LinkContainer } from 'react-router-bootstrap';
import { FaSignOutAlt, FaCogs, FaTasks, FaArchive } from 'react-icons/fa';
// import {archive} from 'react-icons-kit/fa/archive'
import "./NavBar.css";


 class NavBar extends Component {
   render (){
   return  <Navbar fluid collapseOnSelect>
             <Navbar.Header>
               <Navbar.Brand>
                Minipumpar
               </Navbar.Brand>
               <Navbar.Toggle />
             </Navbar.Header>
             <Navbar.Collapse>
               <Nav pullRight>
               <LinkContainer to="/inputs">
                 <NavItem eventKey={1}><FaTasks className="NavBarIcon" /> Ny bokning</NavItem>
               </LinkContainer>
               <LinkContainer to="/waybill">
                 <NavItem eventKey={2}><FaArchive className="NavBarIcon" /> Följesedlar</NavItem>
               </LinkContainer>
                <LinkContainer to="/settings">
                  <NavItem eventKey={3}><FaCogs className="NavBarIcon" /> Inställningar</NavItem>
                </LinkContainer>
                <LinkContainer to="/">
                  <NavItem eventKey={4}><FaSignOutAlt className="NavBarIcon" /> Logga ut</NavItem>
                </LinkContainer>
              </Nav>
             </Navbar.Collapse>
           </Navbar>
    }
}

<i class="fas fa-archive"></i>
export default NavBar;
