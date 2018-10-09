import React, {Component} from "react";
import Waybill from "./Waybill";
import{Grid,Row,Col} from "react-bootstrap"
import { withRouter } from "react-router-dom";

class WaybillPage extends Component{


  render(){
    return (
    <Grid>
      <Row className="show-grid">
        <Col xs={1} md={2}>
          </Col>
            <Col xs={10} md={8}>
                <Waybill/>
            </Col>
          <Col xs={1} md={2}>
        </Col>
      </Row>
    </Grid>
    )
  }
}

export default withRouter(WaybillPage);