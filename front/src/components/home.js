import React from "react";
import PropTypes from 'prop-types';

function load_statuses() {
    document.querySelector('#status-body').value = ''

    fetch('/home')
    .then(response => response.json())
    .then(statuses => {
        statuses.forEach(element => {
            const statusDiv = document.createElement('a');
            statusDiv.id = 'status-' + element.id;
            statusDiv.href = `status/${element.id}`
            statusDiv.className = 'list-group-item list-group-item-action';
            statusDiv.innerHTML = `
                <span>${element.username}</span>
                <span>${element.body}</span>
                <span>${element.timestamp}</span>
            `
            statusDiv.addEventListener('click', () => load_status(element.id))
            container = document.querySelector('.list-group');
            container.insertBefore(statusDiv, container.firstChild);
        })
    })
}

function Home(props) {

    function add_status(e) {
    
        e.preventDefault();
    
        // Parse the status form for content
        const body = document.querySelector('#status-body').value
        const username = document.querySelector('#profile-link').innerHTML

        fetch(`/api/user/${username}/status/`, {
            method: 'POST',
            body: JSON.stringify({
                body: body
            })
        })
        .then(response => response.json())
        .then(result => {
            if (result.error) {
                console.log('Error:', result.error);
                return false;
            }
            console.log(result);
            load_statuses();
        })
    }

    return (
        <div className="home-view">
            <h3>Home</h3>
            <form id="new-status-form" onSubmit={add_status}>
                <div className="form-group">
                    <textarea id="status-body" className="form-control"></textarea>
                    <button type="submit" id="submit" className="btn btn-primary">Post</button>
                </div>
            </form>
            <div id="status-view">
                <div className="list-group"></div>
            </div>
        </div>
    )
}

Home.propTypes = {
    window: PropTypes.func
}

export default Home;