// Code borrowed from the code institute tutorial 'Bootstrap Resume Part 2'

function userInformationHTML(user) {
    return `
    <h2 class="black-text">${user.name}
        <span class="small-name black-text">
            (@<a class="black-text" href="${user.html_url}" target="_blank">${user.login}</a>)
        </span>
    </h2>
    <div class="gh-content">
        <div class="gh-avatar">
            <a href="${user.html_url}" target="_blank">
                <img src="${user.avatar_url}" alt="${user.login}">
            </a>
        </div>
        <p class="black-text">
            Followers: ${user.followers} - Following: ${user.following} <br> 
            Repos: ${user.public_repos}
        </p>
    </div>`;
}

function repoInformationHTML(repos) {
    if (repos.length === 0) {
        return `<div class="clearfix repo-list">No repos!</div>`;
    }
    const listItemsHTML = repos.map(function (repo) {
        return `
        <li>
            <a href="${repo.html_url}" target="_blank">${repo.name}</a>
        </li>
        `;
    });

    return `
    <div class="clearfix repo-list">
        <p class="black-text">
            <strong>Repo List:</strong>
        </p>
        <ul>
            ${listItemsHTML.join("\n")}
        </ul>
    </div>`;
}

function fetchGitHubInformation(event) {

    $("#gh-user-data").html("");
    $("#gh-repo-data").html("");

    const username = $("#gh-username").val();
    if (!username) {
        $("#gh-user-data").html(`<h2 class="black-text">Please enter a GitHub username</h2>`);
        return;
    }

    $("#gh-user-data").html(
        `<div class="progress">
            <div class="indeterminate"></div>
        </div>`
    );

    $.when(
        $.getJSON(`https://api.github.com/users/${username}`),
        $.getJSON(`https://api.github.com/users/${username}/repos`)
    ).then(
        function (firstResponse, secondResponse) {
            const userData = firstResponse[0];
            const repoData = secondResponse[0];
            $("#gh-user-data").html(userInformationHTML(userData));
            $("#gh-repo-data").html(repoInformationHTML(repoData));
        }, function (errorResponse) {
            if (errorResponse.status === 404) {
                $("#gh-user-data").html(
                    `<h2 class="black-text">No info found for user ${username}</h2>`);
            } else if (errorResponse.status === 403) {
                const resetTime = new Date(errorResponse.getResponseHeader("X-RateLimit-Reset") * 1000);
                $("#gh-user-data").html(`<h4 class="black-text">Too many requests made to GitHub API; please wait until ${resetTime.toLocaleTimeString()}</h4>`);
            } else {
                console.log(errorResponse);
                $("#gh-user-data").html(
                    `<h2 class="black-text">Error: ${errorResponse.responseJSON.message}</h2>`);
            }
        }
    );
}

$(document).ready(fetchGitHubInformation)

// Event listener for input change
$(document).ready(function () {
    $("#gh-username").on("input", fetchGitHubInformation);
});