import React, { useCallback } from "react";
import { NavLink } from "react-router-dom";
import PropTypes from "prop-types";

function Nav(props) {

    function getUser() {

    }

    function isLoggedIn() {

    }
    
    const openGoogleLoginPage = useCallback(() => {
        const googleAuthUrl = 'https://accounts.google.com/o/oauth2/v2/auth';
        const redirectUri = 'google/oauth2/callback';
      
        const scope = [
          'https://www.googleapis.com/auth/userinfo.email',
          'https://www.googleapis.com/auth/userinfo.profile'
        ].join(' ');
      
        const params = {
          response_type: 'code',
          client_id: '366642544853-a1kaduj9npl5p1f1ie8eljb2hhpg5d7n.apps.googleusercontent.com',
          redirect_uri: `127.0.0.1:8000/${redirectUri}`,
          prompt: 'select_account',
          access_type: 'offline',
          scope
        };
      
        const urlParams = new URLSearchParams(params).toString();
      
        window.location = `${googleAuthUrl}?${urlParams}`;
      }, []);

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
                <li className="nav-item" onClick={openGoogleLoginPage}>
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