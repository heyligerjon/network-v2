import React from "react";
import PropTypes from 'prop-types';



function add_status(e) {
    
    // e.preventDefault();

    // // Parse the status form for content
    // body = document.querySelector('#status-body').value
    // fetch('/status/new', {
    //     method: 'POST',
    //     body: JSON.stringify({
    //         body: body
    //     })
    // })
    // .then(response => response.json())
    // .then(result => {
    //     if (result.error) {
    //         console.log('Error:', result.error);
    //         return false;
    //     }
    //     console.log(result);
    //     load_statuses();
    // })
}

// function load_statuses() {
//     document.querySelector('#status-body').value = ''

//     fetch('/home')
//     .then(response => response.json())
//     .then(statuses => {
//         statuses.forEach(element => {
//             const statusDiv = document.createElement('a');
//             statusDiv.id = 'status-' + element.id;
//             statusDiv.href = `status/${element.id}`
//             statusDiv.className = 'list-group-item list-group-item-action';
//             statusDiv.innerHTML = `
//                 <span>${element.username}</span>
//                 <span>${element.body}</span>
//                 <span>${element.timestamp}</span>
//             `
//             statusDiv.addEventListener('click', () => load_status(element.id))
//             container = document.querySelector('.list-group');
//             container.insertBefore(statusDiv, container.firstChild);
//         })
//     })
// }

function Home(props) {

    return (
        <div className="home-view">
            <h3>Home</h3>
            <form id="new-status-form">
                <div className="form-group">
                    <textarea id="status-body" className="form-control"></textarea>
                    <button type="submit" id="submit" className="btn btn-primary" onSubmit={add_status()}>Post</button>
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