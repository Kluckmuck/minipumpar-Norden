import React, {Component} from "react";
import Inputs from "./Inputs"
import Header from "./../header/Header"
import{Grid,Row,Col} from "react-bootstrap"
import { withRouter } from "react-router-dom";


class InputPage extends Component{


  render(){
    return (
    <Grid>
      <Row className="show-grid">
        <Col xs={1} md={2}>
          </Col>
            <Col xs={10} md={8}>
<<<<<<< HEAD
=======
                <Header/>
>>>>>>> 39014f3
                <Inputs/>
            </Col>
          <Col xs={1} md={2}>
        </Col>
      </Row>
    </Grid>
    )
  }
}

export default withRouter(InputPage);