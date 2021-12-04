import React from 'react';
import { BrowserRouter as Router, Routes , Route } from "react-router-dom";

import './App.css';
import HomePage from "./pages/HomePage";
import SearchCandidates from "./pages/SearchCandidates";
import SearchJobs from "./pages/SearchJobs";

function App() {
  return (
      <Router basename={process.env.PUBLIC_URL}>
        <div>
          <Routes>
            <Route exact path="/" component={HomePage} />
            <Route path="/search-candidates" component={SearchCandidates} />
            <Route path="/search-jobs" component={SearchJobs} />
          </Routes>
        </div>
      </Router>
  );
}

export default App;
