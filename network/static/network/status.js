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

    // Clear out text field
    document.querySelector('#comment-body').value = ''

    // Display the comment box and add a click handler to send button
    document.querySelector('#comment-box').style.display= 'block'
}

function reply(statusId) {

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
        //load_status(statusId)
    })
    window.location.reload()
}

function react(statusId) {

}

// function load_status(statusId) {

//     fetch(`${statusId}`)
//         // add comment to list group and hide editor
//         const commentDiv = document.createElement('div');
//         commentDiv.id = `comment-${statusId}-${result.commentId}`;
//         commentDiv.className = 'list-group-item list-group-item-action';
//         commentDiv.innerHTML = `
//             <h6 class="card-title">${username}</h6>
//             <p class="card-text">${body}</span>
//         `;
//         container = document.querySelector('#comment-list');
//         container.append(commentDiv);
//         document.querySelector('#comment-box').style.display = 'none';
// }

function edit_status(statusId) {

}