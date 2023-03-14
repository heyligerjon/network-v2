import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Nav from './src/components/nav.js'
import Login from './src/components/login.js'
import Register from './src/components/register.js';
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
        <Route path='/login' element={<Login />}/>
        <Route path='/register' element={<Register />}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
