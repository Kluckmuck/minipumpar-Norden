import React from 'react';
// import ReactDOM from 'react-dom';
import Login from "./components/Login.jsx";
import Inputs from "./components/Inputs.jsx";
import { HashRouter as Router, Route } from 'react-router-dom';
// import registerServiceWorker from './registerServiceWorker';
import Settings from "./components/Settings.jsx";
// import routes from "./routes";
export default  ( <Router>
    <div>
      <Route exact path="/" component={Login}></Route>
      <Route path="/inputs" component={Inputs}></Route>
      <Route path="/settings" component={Settings}></Route>
    </div>
</Router>)
