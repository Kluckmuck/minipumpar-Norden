import React, {Component} from "react";
import Settings from "./Settings.jsx"
import{Grid,Row,Col} from "react-bootstrap"
import { withRouter } from "react-router-dom";

class SettingsPage extends Component{


  render(){
    return (
    <Grid>
      <Row className="show-grid">
        <Col xs={2} md={4}>
          </Col>
            <Col xs={8} md={4}>
                <Settings/>
            </Col>
          <Col xs={2} md={4}>
        </Col>
      </Row>
    </Grid>
    )
  }
}

export default withRouter(SettingsPage);