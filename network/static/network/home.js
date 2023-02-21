document.addEventListener('DOMContentLoaded', () => {

    // Use buttons to toggle between views
    document.querySelector('#new-status-form').addEventListener('submit', add_status);

    // By default, load the statuses
    load_statuses();
});

function add_status(e) {
    
    e.preventDefault();

    // Parse the status form for content
    body = document.querySelector('#status-body').value
    fetch('/status/new', {
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

function load_statuses() {

    fetch('/home')
    .then(response => response.json())
    .then(statuses => {
        statuses.forEach(element => {
            const statusDiv = document.createElement('div');
            statusDiv.id = 'status-' + element.id;
            statusDiv.className = 'list-group-item';
            statusDiv.innerHTML = `
                <span>${element.username}</span>
                <span>${element.body}</span>
                <span>${element.timestamp}</span>
            `
            statusDiv.addEventListener('click', () => load_status(element.id))
            container = document.querySelector('#status-view');
            container.insertBefore(statusDiv, container.firstChild);
        })
    })
}