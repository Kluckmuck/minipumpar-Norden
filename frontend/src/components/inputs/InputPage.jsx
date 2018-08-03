import React, {Component} from "react";
import Inputs from "./Inputs.jsx"
import{Grid,Row,Col} from "react-bootstrap"
import { withRouter } from "react-router-dom";

class InputPage extends Component{


  render(){
    return (
    <Grid>
      <Row className="show-grid">
        <Col xs={2} md={4}>
          </Col>
            <Col xs={8} md={4}>
                <Inputs/>
            </Col>
          <Col xs={2} md={4}>
        </Col>
      </Row>
    </Grid>
    )
  }
}

export default withRouter(InputPage);