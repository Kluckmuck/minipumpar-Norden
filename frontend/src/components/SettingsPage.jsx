import React, {Component} from "react";
import Settings from "./Settings.jsx"
import{Grid,Row,Col} from "react-bootstrap"
import { withRouter } from "react-router-dom";

class SettingsPage extends Component{


  render(){
    return (
    <Grid>
      <Row className="show-grid">
        <Col xs={1} md={2}>
          </Col>
            <Col xs={10} md={8}>
                <Settings/>
            </Col>
          <Col xs={1} md={2}>
        </Col>
      </Row>
    </Grid>
    )
  }
}

export default withRouter(SettingsPage);