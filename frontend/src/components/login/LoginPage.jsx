import React, {Component} from "react";
import Login from "./Login.jsx"
import{Grid,Row,Col} from "react-bootstrap"
import { withRouter } from "react-router-dom";

class LoginPage extends Component{

  render(){
    return (
      <Grid>
        <Row className="show-grid">
          <Col xs={2} md={4}>
            </Col>
              <Col xs={8} md={4}>
                  <Login/>
              </Col>
            <Col xs={2} md={4}>
          </Col>
        </Row>
      </Grid>
    )
  }
}

export default withRouter(LoginPage);