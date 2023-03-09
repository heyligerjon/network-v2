import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Nav from './src/components/nav.js'
import Home from "./src/components/home.js"
import Profile from "./src/components/profile.js"
import Status from "./src/components/status.js"
//import './static/css';

function App(props) {
  return (
    <BrowserRouter>
      <Nav /> 
      <Routes>
        <Route path='/' element={<Home />}/>
      </Routes>
    </BrowserRouter>  
  );
}

export default App;
