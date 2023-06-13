//Initialise modals
document.addEventListener('DOMContentLoaded', function () {
    let modals = document.querySelectorAll('.modal');
    let modalsInstances = M.Modal.init(modals);
});

//Open Edit Warning Modals
document.addEventListener('DOMContentLoaded', function () {
    const editBlog = document.getElementById('editblogmodal');
    let instance = M.Modal.init(editBlog);
    instance.open();
});

document.addEventListener('DOMContentLoaded', function () {
    const editJob = document.getElementById('editjobmodal');
    let instance = M.Modal.init(editJob);
    instance.open();
});

//Initialise dropdown
document.addEventListener('DOMContentLoaded', function () {
    let dropdowns = document.querySelectorAll('.dropdown-trigger');
    let dropdownsInstances = M.Dropdown.init(dropdowns);
});

//Initialise sidenav
document.addEventListener('DOMContentLoaded', function () {
    let sidenavs = document.querySelectorAll('.sidenav');
    var sidenavInstances = M.Sidenav.init(sidenavs);
});

//Fix bug that doesn't auto-apply materialize styles to textareas
let textareas = document.querySelectorAll('.textarea');
for (let i = 0; i < textareas.length; i++) {
    textareas[i].className = 'materialize-textarea';
}

//Alter form labels to be a darker shade.
let labels = document.querySelectorAll('label');
for (let i = 0; i < labels.length; i++) {
    labels[i].className = 'black-text';
}

//Remove asterisks from forms
let asterisks = document.querySelectorAll('.asterisk');
for (let asterisk of asterisks) {
    asterisk.remove();
}

//Messages disappear after 3 seconds.
setTimeout(function () {
    let message = document.getElementById("msg");
    message.remove();
}, 3000);

document.addEventListener('DOMContentLoaded', function () {
    const applyButton = document.getElementById('apply');
    applyButton.addEventListener('mouseenter', () => {
        console.log(applyButton);
        M.toast({ html: 'WARNING: Once you submit, You cannot change your application!', classes: 'red darken-4' });
    });
});

document.addEventListener('DOMContentLoaded', function () {
    // Alert the user to the permanent deletion of account.
    const deleteButton = document.getElementById('delete');
    deleteButton.addEventListener('mouseenter', () => {
        console.log('hello');
        M.toast({ html: 'WARNING: This action is not reversible.', classes: 'red darken-4' });
    });

});

let jobSeekerDiv = document.getElementById('div_id_job_seeker');
let jobSeekerInput = document.getElementById('id_job_seeker');
jobSeekerDiv.replaceWith(jobSeekerInput);

let recruiterDiv = document.getElementById('div_id_recruiter');
let recruiterInput = document.getElementById('id_recruiter');
recruiterDiv.replaceWith(recruiterInput);