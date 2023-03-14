import React from "react";
import ProTypes from 'prop-types';

function register() {
    
}

export default function Register(props) {

    return(
        <div>
            <h2>Register</h2>
                {/* {% if error %}
                    <div>{{ error }}</div>
                {% endif %} */}
                <form onSubmit={register} method="post">
                    <div className="form-group">
                        <input className="form-control" autoFocus type="text" name="username" placeholder="Username"/>
                    </div>
                    <div className="form-group">
                        <input className="form-control" type="email" name="email" placeholder="Email Address"/>
                    </div>
                    <div className="form-group">
                        <input className="form-control" type="password" name="password" placeholder="Password"/>
                    </div>
                    <div className="form-group">
                        <input className="form-control" type="password" name="confirmation" placeholder="Confirm Password"/>
                    </div>
                    <input className="btn btn-primary" type="submit" value="Register"/>
                </form>

                Already have an account? <a href="login">Log In here.</a>
        </div>
    )
}