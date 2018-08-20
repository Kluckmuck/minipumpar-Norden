import React, {Component} from "react";
import Login from "./Login"
import{Grid,Row,Col} from "react-bootstrap"
import { withRouter } from "react-router-dom";
import Header from "../images/Header"
class LoginPage extends Component{

  render(){
    return (
      <Grid>
        <Row className="show-grid">
          <Col xs={1} md={2}>
            </Col>
              <Col xs={10} md={8}>
              <Header/>
                  <Login/>
              </Col>
            <Col xs={1} md={2}>
          </Col>
        </Row>
      </Grid>
    )
  }
}

export default withRouter(LoginPage);