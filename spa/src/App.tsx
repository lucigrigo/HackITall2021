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

            <Route path="/">
                <HomePage />
            </Route>

            <Route path="/search-candidates">
              <SearchCandidates />
            </Route>

            <Route path="/search-jobs">
                <SearchJobs />
            </Route>

          </Routes>
        </div>
      </Router>
  );
}

export default App;
