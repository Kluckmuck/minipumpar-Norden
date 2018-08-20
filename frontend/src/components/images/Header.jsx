import React , {Component} from "react";
import Picture from "./minipumpmedlogo.svg"
import "../css/Header.css"
import{Grid,Row,Col} from "react-bootstrap"
export default class Header extends Component{

    render() {
        return <div>
        <Grid>
            <Row className="show-grid">
              <Col xs={1} md={2}>
                </Col>
                  <Col xs={10} md={8}>
                    <img src={Picture} className="svg1 center"  />
                  </Col>
                <Col xs={1} md={2}>
              </Col>
            </Row>
      </Grid>
        </div>
    }
    
};
