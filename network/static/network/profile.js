document.addEventListener('DOMContentLoaded', () => {

    // Use buttons to toggle between views
    document.querySelector('#profile-li').addEventListener('click', () => 
        load_profile(document.querySelector('#profile-link').value));

    // By default, load the user's profile
    load_profile(document.querySelector('#profile-link').innerHTML);
});

function load_profile(username) {

    // document.querySelector
    // var user = '';

    // if (username == '')
    //     user = document.querySelector('#profile-link').innerHTML;
    // else 
    //     user = username;

    // fetch(`/user/${username}`)
    // .then(response => response.json())
    // .then(result => {
    //     const profileDiv = document.createElement('div');
    //     profileDiv.id = `user-profile-${user}`
    //     profileDiv.innerHTML = `
    //         TODO
    //     `
    //     document.querySelector('#profile-view').append(profileDiv);
    // })
}