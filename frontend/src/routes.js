import React from 'react';
import { Route } from 'react-router';
import Login from "./components/Login.jsx"
import Inputs from "./components/Inputs.jsx"
import Settings from "./components/Settings.jsx"
export default (
  <Route path="/" component={Login}>
    {/* <IndexRoute component={Greetings} /> */}
    <Route path="/inputs" component={Inputs}></Route>
    <Route path="/settings" component={Settings}></Route>
  </Route>
)