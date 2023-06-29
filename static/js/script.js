function initializeModals() {
    let modals = document.querySelectorAll('.modal');
    let modalsInstances = M.Modal.init(modals);
}

function initializeDropdowns() {
    let dropdowns = document.querySelectorAll('.dropdown-trigger');
    let dropdownsInstances = M.Dropdown.init(dropdowns);
}

function initializeSidenavs() {
    let sidenavs = document.querySelectorAll('.sidenav');
    var sidenavInstances = M.Sidenav.init(sidenavs);
}

function fixTextareas() {
    let textareas = document.querySelectorAll('.textarea');
    if (textareas.length > 0) {
        for (let i = 0; i < textareas.length; i++) {
            textareas[i].className = 'materialize-textarea';
        }
    }
}

function fixLabels() {
    let labels = document.querySelectorAll('label');
    if (labels.length > 0) {
        for (let i = 0; i < labels.length; i++) {
            labels[i].classList.add('active');
            labels[i].classList.add('black-text');
        }
    }
}

function fixAsterisks() {
    let asterisks = document.querySelectorAll('.asterisk');
    for (let asterisk of asterisks) {
        asterisk.remove();
    }
}

function messageTimeout() {
    setTimeout(function () {
        let message = document.getElementById("msg");
        if (message != null) {
            message.remove();
        }
    }, 3000);
}

function applicationToast() {
    const applyButton = document.getElementById('apply');
    applyButton.addEventListener('mouseenter', () => {
        console.log(applyButton);
        M.toast({ html: 'WARNING: Once you submit, You cannot change your application!', classes: 'red darken-4' });
    });
}

function deletionToast() {
    const deleteButton = document.getElementById('delete');
    deleteButton.addEventListener('mouseenter', () => {
        console.log('hello');
        M.toast({ html: 'WARNING: This action is not reversible.', classes: 'red darken-4' });
    });
}

function fixCheckboxJobSeeker() {
    let jobSeekerDiv = document.getElementById('div_id_job_seeker');
    let jobSeekerInput = document.getElementById('id_job_seeker');
    jobSeekerDiv.replaceWith(jobSeekerInput);
}

function fixCheckboxRecruiter() {
    let recruiterDiv = document.getElementById('div_id_recruiter');
    let recruiterInput = document.getElementById('id_recruiter');
    recruiterDiv.replaceWith(recruiterInput);
}


document.addEventListener('DOMContentLoaded', function(){

    try {
        initializeModals();
    } catch(error){
        //pass - no errors reported to console
    }

    try {
        initializeDropdowns();
    } catch (error) {
        //pass - no errors reported to console
    }

    try {
        initializeSidenavs();
    } catch (error) {
        //pass - no errors reported to console
    }

    try {
        fixTextareas();
    } catch (error) {
        //pass - no errors reported to console
    }

    try {
        fixLabels();
    } catch (error) {
        //pass - no errors reported to console
    }

    try {
        fixAsterisks();
    } catch (error) {
        //pass - no errors reported to console
    }

    try {
        messageTimeout();
    } catch (error) {
        //pass - no errors reported to console
    }

    try {
        applicationToast();
    } catch (error) {
        //pass - no errors reported to console
    }

    try {
        deletionToast();
    } catch (error) {
        //pass - no errors reported to console
    }

    try {
        fixCheckboxJobSeeker();
    } catch (error) {
        //pass - no errors reported to console
    }

    try {
        fixCheckboxRecruiter();
    } catch (error) {
        //pass - no errors reported to console
    }

});
