document.addEventListener('DOMContentLoaded', () => {

    const statusId = document.querySelector('#status-id').innerHTML

    // Use buttons to toggle between views
    document.querySelector('#status-reply').addEventListener('click', () => 
        open_reply(statusId));
    document.querySelector('#status-like').addEventListener('click', () => 
        react(statusId));
    document.querySelector('#status-edit').addEventListener('click', () => 
        edit_status(statusId));
    
    document.querySelector('#comment-form').addEventListener('submit', () => {
        reply(statusId);
    });
    // Hide the comment box initially
    document.querySelector('#comment-box').style.display= 'none'
});

function open_reply(statusId) {
    
    // Display the comment box and add a click handler to send button
    document.querySelector('#comment-box').style.display= 'block'
}

function reply(statusId) {
    event.preventDefault()
    // Parse document and form for parameters and POST
    username = document.querySelector('#status-user').innerHTML
    body = document.querySelector('#comment-body').value

    fetch(`${statusId}/comment`, {
        method: 'POST',
        body: JSON.stringify({
            username: username,
            body: body,
        })
    })
    .then(response => response.json())
    .then(result => {
        if (result.error) {
            console.log('Error:', result.error);
            return false;
        }
        console.log(result);
        document.querySelector('#comment-box').style.display = 'none'
        // add comment to list group
        //load_status(statusId);
    })
    return false;
}

function react(statusId) {

}

function load_status(statusId) {

}

function edit_status(statusId) {

}