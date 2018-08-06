import React, {Component} from "react";
import Login from "./Login.jsx"
import{Grid,Row,Col} from "react-bootstrap"
import { withRouter } from "react-router-dom";

class LoginPage extends Component{

  render(){
    return (
      <Grid>
        <Row className="show-grid">
          <Col xs={1} md={2}>
            </Col>
              <Col xs={10} md={8}>
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