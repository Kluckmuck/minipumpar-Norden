import React, {Component} from "react";


var site  = 'http://maxjou.se:8000';
class Logout extends Component {
   componentDidMount(){
     fetch(site + "/api/logout/",{
       credentials:"include"
     }).then(response =>{
      return response.json();
     }).then(()=>{
       this.props.history.push("/")
     })
   }

   render(){
    return <div>

    </div>
   }
 }

export default Logout


