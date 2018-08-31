import React , {Component} from "react";
import Picture from "./minipumpartext.svg"
import "./Header.css"
export default class Header extends Component{

    render() {
        return <div>
             <img src={Picture} className="svg1 center"  />
        </div>
    }
    
};
