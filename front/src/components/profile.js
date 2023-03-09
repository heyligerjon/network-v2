// document.addEventListener('DOMContentLoaded', () => {

//     username = document.querySelector('#user-hdr').innerHTML;

//     // Use buttons to toggle between views
//     document.querySelector('#friends-count').addEventListener('click', () =>
//         load_friends(document.querySelector('#user-hdr').innerHTML));

//     document.querySelector('#profile-edit').addEventListener('click', () =>
//         load_editor());
//     document.querySelector('#profile-edit-form').addEventListener('submit', (event) =>{
//         event.preventDefault()
//         edit_profile(username)
//     });

//     // By default, load the user's profile
//      load_profile();
// });

// function load_profile() {

//     // Hide the friends view and display the profile
//     document.querySelector('#profile-view').style.display = 'block'
//     document.querySelector('#profile-editor').style.display = 'none'
//     document.querySelector('#friends-view').style.display = 'none'
// }

// function load_friends(username) {

//     // Show the friends view and hide the profile
//     document.querySelector('#friends-view').style.display = 'block'
//     document.querySelector('#profile-view').style.display = 'none'

//     fetch(`${username}/friends`)
//     .then(response => response.json())
//     .then(context => {
//         if (context.error) {
//             console.log('Error:', context.error);
//             return false;
//         }
//         const friends = JSON.parse(context.data)
//         friends.forEach(element => {
//             //
//             //if (element.fields.username == username)
//             //     return;

//             console.log(element.fields.username);
//             const friendDiv = document.createElement('a');
//             friendDiv.id = `${username}-friend-${element.id}`
//             friendDiv.href = `/user/${element.username}`
//             friendDiv.className = 'list-group-item list-group-item-action'
//             friendDiv.innerHTML = `
//                 <span>${element.fields.username}</span>
//                 <span>${element.fields.first_name}</span>
//                 <span>${element.fields.last_name}</span>
//             `
//             container = document.querySelector('#friend-list-group');
//             container.insertBefore(friendDiv, container.firstChild);
//         })

//     })
// }

// function load_editor() {

//     // Hide profile view and show edit form
//     document.querySelector('#profile-editor').style.display = 'block'
//     document.querySelector('#profile-view').style.display = 'none'
//     document.querySelector('#friends-view').style.display = 'none'
// }

// function edit_profile(username) {

//     // Retrieve data from form
//     // change to parse all form fields and create dict of values
//     // add handling for empty fields
//     user = document.querySelector('#field-user').value

//     if (user == '')
//         user = username

//     firstName = document.querySelector('#field-first').value
//     lastName = document.querySelector('#field-last').value
//     email = document.querySelector('#field-email').value
//     csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

//     // Revert to profile view after submitting
//     document.querySelector('#profile-view').style.display = 'block'
//     document.querySelector('#profile-editor').style.display = 'none'
//     document.querySelector('#friends-view').style.display = 'none'

//     // Clear fields and set placeholders to new values
//     document.querySelectorAll('.form-control').forEach(field => {
//         field.setAttribute('placeholder', field.value)
//         field.value = ''
//     })

//     fetch(`${username}/edit`, {
//         method: 'POST',
//         headers: {"X-CSRFToken": csrftoken},
//         body: JSON.stringify({
//             "username": user,
//             "firstName": firstName,
//             "lastName": lastName,
//             "email": email
//         })
//     })
//     .then(response => response.json())
//     .then(result => {
//         if (result.error) {
//             console.log('Error:', result.error);
//             return false;
//         }
//         console.log(result.message);
//     })
// }