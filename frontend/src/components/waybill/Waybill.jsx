import React ,{Component} from "react"
import { withRouter } from "react-router-dom";
import "./Waybill.css"

class Waybill extends Component {
    constructor (props){
        super(props);
    }
    render (){
        return (
            <div>
                <h1>Component works!</h1>
            </div>
        )
    }
}

export default withRouter(Waybill);