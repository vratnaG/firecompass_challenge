import React from "react"
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom'
import Home from "./component/Home";

function App() {
  return <Router>
    <div className="App">
      <Switch>
        <Route path="/" exact component={Home} />
      </Switch>
    </div>
  </Router>
}

export default App;
