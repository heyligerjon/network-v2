document.addEventListener('DOMContentLoaded', () => {

    // Use buttons to toggle between views
    document.querySelector('#friends-count').addEventListener('click', () => 
        load_friends(document.querySelector('#user-hdr').innerHTML));
    
    document.querySelector('#user-username').addEventListener('click', () => 
        load_profile());

    // By default, load the user's profile
     load_profile();
});

function load_profile() {

    // Hide the friends view and display the profile 
    document.querySelector('#profile-view').style.display = 'block'
    document.querySelector('#friends-view').style.display = 'none'   
}

function load_friends(username) {

    // Show the friends view and hide the profile
    document.querySelector('#friends-view').style.display = 'block'
    document.querySelector('#profile-view').style.display = 'none'

    fetch(`${username}/friends`)
    .then(response => response.json())
    .then(context => {
        if (context.error) {
            console.log('Error:', context.error);
            return false;
        }
        const friends = JSON.parse(context.data)
        friends.forEach(element => {
            //  
            //if (element.fields.username == username)
            //     return;

            console.log(element.fields.username);
            const friendDiv = document.createElement('a');
            friendDiv.id = `${username}-friend-${element.id}`
            friendDiv.href = `/user/${element.username}`
            friendDiv.className = 'list-group-item list-group-item-action'
            friendDiv.innerHTML = `
                <span>${element.fields.username}</span>
                <span>${element.fields.first_name}</span>
                <span>${element.fields.last_name}</span>
            `
            container = document.querySelector('#friend-list-group');
            container.insertBefore(friendDiv, container.firstChild);
        })

    })
}

function edit_profile(username) {
    
}