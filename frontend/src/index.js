import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import Login from "./components/login/LoginPage.jsx";
import Logout from "./components/Logout.jsx";
import Inputs from "./components/inputs/InputPage.jsx";
import Settings from "./components/SettingsPage.jsx";
import { HashRouter as Router, Route } from 'react-router-dom';
import registerServiceWorker from './registerServiceWorker';
import ConfirmationPage from "./components/confirmation/ConfirmationPage.jsx";

ReactDOM.render(  <Router>
    <div>
      <Route exact path="/" component={Login}></Route>
      <Route path="/inputs" component={Inputs}></Route>
      <Route path="/logout" component={Logout}></Route>
      <Route path="/settings" component={Settings}></Route>
      <Route path="/confirmationPage" component={ConfirmationPage}></Route>
    </div>
</Router>, document.getElementById('app'));
registerServiceWorker();
