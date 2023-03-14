import React from "react";
import PropTypes from 'prop-types';

function login() {

}

function Login(props) {

    return(
        <div>
            <h2>Login</h2>
                {/* <div>{error_message}</div> */}

            <form onSubmit={login} method="post">
                <div className="form-group">
                    <input autoFocus className="form-control" type="text" name="username" placeholder="Username"/>
                </div>
                <div className="form-group">
                    <input className="form-control" type="password" name="password" placeholder="Password"/>
                </div>
                <input className="btn btn-primary" type="submit" value="Login"/>
            </form>

            Don't have an account? <a href="register">Register here.</a>
        </div>
    )
}

Login.propTypes = {
    window: PropTypes.func
}

export default Login;