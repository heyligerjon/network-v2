import React from "react";
import PropTypes from "prop-types";

function Nav(props) {
    return (
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <a class="navbar-brand" href="#">Network</a>
            <div>
              <ul class="navbar-nav mr-auto">
                <li class="nav-item">
                  <a class="nav-link" href="{% url 'index' %}">Timeline</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Following</a>
                </li>
              </ul>
            </div>
        </nav>
    )
}