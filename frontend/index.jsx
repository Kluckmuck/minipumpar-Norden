import React from "react";
import ReactDOM from "react-dom";
import Login from "./components/Login.jsx";
import Inputs from "./components/inputs.jsx";
import { HashRouter as Router, Route } from 'react-router-dom'
ReactDOM.render(
  <Router>
    <div>
      <Route exact path="/" component={Login}></Route>
      <Route path="/inputs" component={Inputs}></Route>
    </div>
</Router>,
  document.getElementById('app')
);