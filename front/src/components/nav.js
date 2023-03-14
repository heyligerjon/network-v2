import React from "react";
import { NavLink } from "react-router-dom";
import PropTypes from "prop-types";

function Nav(props) {

    function getUser() {

    }

    function isLoggedIn() {

    }

    return (
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <a className="navbar-brand" href="#">Network</a>
            <div>
              <ul className="navbar-nav mr-auto">

                 <li id="profile-li" className="nav-item">
                    <NavLink 
                      to={`/username/`}
                      id="profile-link" 
                      className="nav-link" 
                      style={{fontWeight: 'bold'}}
                    >
                        Username
                    </NavLink>
                </li>
                <li className="nav-item">
                  <NavLink to={"/"} id="tl-link" className="nav-link">
                    Timeline
                  </NavLink>
                </li>
                <li className="nav-item">
                    <a className="nav-link" href="#">Following</a>
                </li>
                <li className="nav-item">
                        <a className="nav-link">Log Out</a>
                </li>
                <li className="nav-item">
                    <NavLink to={"/login"} id="login-link" className="nav-link">
                        Log In
                    </NavLink>
                </li>
                <li className="nav-item">
                    <NavLink to={"/register"} id="register-link" className="nav-link">
                        Register
                    </NavLink>
                </li>
              </ul>
            </div>
        </nav>
    )
}

Nav.propTypes = {
    username: PropTypes.string
}

export default Nav;