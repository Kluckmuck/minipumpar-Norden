import React ,{Component} from "react";
import { withRouter } from "react-router-dom";
import NavBar from "./../navbar/NavBar";
import "./Waybill.css";

class Waybill extends Component {
    constructor (props){
        super(props);
        this.state ={

        }
    }

    componentDidMount(){
        
    }
    render (){
        return (
            <div className="Waybill">
                <br/>
                    <NavBar/>
                <br/>
                <h1>Component works!</h1>
                <p>Leta upp en gammal följesedel.</p>
            </div>
        )
    }
}

export default withRouter(Waybill);