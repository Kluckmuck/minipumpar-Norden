import React, {Component} from "react";
import Confirmation from "./Confirmation"
import{Grid,Row,Col} from "react-bootstrap"
import { withRouter } from "react-router-dom";

class ConfirmationPage extends Component{

  render(){
    return (
      <Grid>
        <Row className="show-grid">
          <Col xs={1} md={2}>
            </Col>
              <Col xs={10} md={8}>
                  <Confirmation/>
              </Col>
            <Col xs={1} md={2}>
          </Col>
        </Row>
      </Grid>
    )
  }
}

export default withRouter(ConfirmationPage);