document.addEventListener('DOMContentLoaded', () => {

    // Use buttons to toggle between views
    document.querySelector('#new-status-form').addEventListener('submit', add_status);

    // By default, load the inbox
    load_statuses;
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

}