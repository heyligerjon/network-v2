import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from "./src/components/home.js"
import Profile from "./src/components/profile.js"
import Status from "./src/components/status.js"
//import './static/css';

function App(props) {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Home />}/>
      </Routes>
    </BrowserRouter>  
  );
}

export default App;
