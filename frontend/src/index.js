import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import Login from "./Login.jsx";
import Inputs from "./Inputs.jsx";
import { HashRouter as Router, Route } from 'react-router-dom'
import registerServiceWorker from './registerServiceWorker';

ReactDOM.render(  <Router>
    <div>
      <Route exact path="/" component={Login}></Route>
      <Route path="/inputs" component={Inputs}></Route>
    </div>
</Router>, document.getElementById('app'));
registerServiceWorker();
