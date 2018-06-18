import React from "react";
// import input from 'react-bootstrap/lib/input';


class Input extends React.Component {
  render() {
    return(
    <form> 
      <div className="form-group">
        <label htmlFor="date">Datum:</label>
        <input type="text" className="form-control" id="date"/>
      </div>
       <div className="form-group">
        <label htmlFor="LittNr">Litt Nr:</label>
        <input type="text" className="form-control" id="LittNr"/>
      </div>
      <div className="form-group">
        <label htmlFor="ArbetsNr">Arbets Nummer::</label>
        <input type="text" className="form-control" id="ArbetsNr"/>
      </div>
    </form>);
  }
}

module.exports ={ Input:Input };
