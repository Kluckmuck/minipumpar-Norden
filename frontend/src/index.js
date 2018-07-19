import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import Login from "./Login.jsx";
import Inputs from "./Inputs.jsx";
import { HashRouter as Router, Route } from 'react-router-dom';
import registerServiceWorker from './registerServiceWorker';
import Settings from "./components/Settings.jsx";

ReactDOM.render(  <Router>
    <div>
      <Route exact path="/" component={Login}></Route>
      <Route path="/inputs" component={Inputs}></Route>
      <Route path="/settings" component={Settings}></Route>
    </div>
</Router>, document.getElementById('app'));
registerServiceWorker();
