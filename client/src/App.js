import React from "react";

import LoginForm from './components/auth/Login'
import {
  BrowserRouter as Router,
  Switch,
  Route
} from "react-router-dom";
import TopNavbar from "./components/common/TopNavbar";
import SignupForm from "./components/auth/Signup";
import HomeView from "./views/HomeView";

import './styles/main.css'

function App() {
  return (
    <Router>
      <TopNavbar/>
      <div className="app-container">
        {/* A <Switch> looks through its children <Route>s and
            renders the first one that matches the current URL. */}
        <Switch>
          <Route path="/login">
            <LoginForm />
          </Route>
          <Route path="/signup">
            <SignupForm />
          </Route>

          <Route path="/">
            <HomeView/>
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

export default App;
