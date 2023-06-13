# **Devs and Roles**

Developed by Jeremy Simons

<img src="docs/amiresponsivepp3.png" alt="A screenshot of Am I Responsive representation of the website">

[Link to live site](https://devs-and-roles.herokuapp.com/)

## Introduction

Devs and Roles is the proposed solution to platforms such as linkedIn which generate too much noise from professionals who are not from the tech industry. It aims to provide a community for software developers and other tech professionals to, firstly, gain access to new job opportunities. Secondly, the site aims to connect with tech professionals with other tech professionals and recruiters who are actively seeking quality talent for their clients or companies.

With the blog feature, it allows professionals and recruiters alike to market themselves with long-format, high-quality content rather than the sound-bite feed of memes and platitudes on other platforms. Recruiters have the ability to search through a catalogue of job-seeking users to connect with them directly.

The ultimate goal of these features is to expedite the recruitment process for tech workers and recruiters alike.

## Contents

* [Project Goals](#project-goals)<br>
    * [For the user](#for-the-user)
    * [For the site owner](#for-the-site-owner)
* [User Experience](#user-experience)<br>
    * [Target audience](#target-audience)
    * [User requirements](#user-requirements)
    * [User Manual](#user-manual)
    * [User Stories](#user-stories)
* [Design](#design)
    * [wireframes](#wireframes)
* [Technical Design](#technical-design)
    * [Data Models](#data-models)
    * [Database Schema](#database-schema)
* [Features](#features)
    * [App Features](#app-features)
    * [Feature Ideas for future development](#feature-ideas-for-future-development)
* [Technologies Used](#technologies-used)
* [Deployment & Local Development](#deployment--local-development)
* [Testing](#testing)
    * [Validation](#validation)
    * [Manual Testing](#manual-testing)
    * [Automated Testing](#automated-testing)
    * [Bugs](#bugs)
* [Credits](#credits)

## Project Goals

### ...For the user

* To view job openings and apply for them to progress in one's own career
* To gain access to potential candidates for a tech role that I may be needing to fill.
* To interact with other members of the software development and hiring community in order to expand professional networks.

### ...For the site owner

* To provide a platform for tech recruiters and tech workers to interact and to facilitate the hiring process.
* To keep users safe from malicious or inappropriate content by having the ability to report and remove user-made content.

## User Experience

### Target audience

The target audience of this website is threefold:
    1. Non-committed users who just want to browse the job market without signing up or applying.
    2. Committed job-seekers who are actively pursuing job opportunities.
    3. Recruiters who are seeking to attract talent to their companies or clients.

### User requirements

* Users must be able to share their thoughts/work/expertise in a community which allows them to interact and network with other users.
* Users must have features tailored to what their aims are.
* As job-seekers they must be able to apply for jobs and keep track of their applications.
* As recruiters they must be able to view and message candidates via their candidate profiles. They must also be able to track who has applied to their job postings as well as view the details of each application.

### User Manual

Click the dropdown to view the user manual:
<details>
<summary>User Manual</summary>

### Home page

When accessing the site for the first time users will arrive on the home page and will be able to scroll through the job listings as well as click on each one to view the details. Apart from this the user will not be able to interact with the site and the navbar will only display the home option.

The user may access any links in the footer, however they will not be able to submit a valid contact form without first signing up.

### Login/register

When registering, users must fill out the form providing username, email and password. Username and password will be needed to subsequently log back into the account.

### Complete the user profile

Upon registering a new account, the user will be directed to the profile creation page. Not only will this provide information that other site users can view, it will determine which site features are available to users (by selecting job-seeker or recruiter options respectively).

### Access site features

* All users will have access to the blog community. Users can create, peruse, update and delete their blogs.
* All users will have access to the commenting feature on all blog posts. Note that any inappropriate posts or comments are reportable and may be removed from the site by the admin if necessary.
* All users will have access to the contact form to raise issues with the site admin.
* if you selected recruiter you will now be able to create, update, and delete job postings, view candidate profiles, and message candidates.
  * Please note that job postings are reportable and may be removed without warning if deemed inappropriate, malicious, or fake.
* if you selected job-seeker you will now be able to apply for job postings and view a list of your current applications.

### Notifications

Upon completing any of the above actions, the user should be notified with a popup message. These are set to auto close after 3 seconds.

</details><br>

### User Stories

#### As a job-seeker user...

(1) As a new user I want to sign up to the job board so that I can view new job openings.

(2) As a job seeker I want to view a paginated list of job opportunities so that I can find a role suitable for me.

(3) As a job seeker I want to create a profile so that employers can find out more about me.

(4) As a job seeker I want to easily navigate between job postings and my profile so that I can access the features I need.

(5) As a job seeker I want to see which jobs I have already applied for so that I can keep track of the application/follow it up.

(6) As a job seeker I want to fill out a form to apply for a job, so that I can be considered for it by the employer.

(7) As a job seeker I want to be able to see how many other applicants have already applied to each role on the job board.

(8) As a jobseeker I want to withdraw my application so that I can notify the employer I no longer wish to be considered for the role.

(9) As a job seeker/recruiter I want to be able to create a blog post so that I can show employers more of my interest/skills or attract talent.

(10) As a job seeker/recruiter I want to comment on blog posts so that I can interact with other users.

(11) As a jobseeker I want to report any suspicious or malicious posts on the job board.

(12) As the job seeker I want to contact the site owner about potential problems/bugs with the site so that they can be fixed.

#### As a recruiter user... 

(13) As a new user I want to sign up to the job board so that I can post new jobs and view profiles of existing candidates so that I can fill a role.

(14) As an employer I want to create a job posting that can be approved and added to the job board so that I can advertise a role.

(15) As an employer I want to take down a job posting when I have filled the role so that I don't get swamped with unnecessary applications for a job.

(16) As an employer I want to edit my job posting so that I can keep it up to date with the requirements of the role I want to fill.

(17) As an employer I want to scroll through a paginated list of candidates so that I can find a good fit for my open position.

(18) As an employer I want to be able to send messages to potential candidates so that I can advertise roles that might be a good fit.

(19) As an employer I want to see how many candidates have applied to each job I post so that I can gauge which of my advertised roles are the most popular.

(20) As a recruiter or job seeker I want to delete my account if I no longer wish to use the service so that I can remove my personal data from the website.

(21) As a recruiter or job seeker I want to update my account details so that I can use my most up-to-date contact details, etc.

#### As the site owner...

(22) As the site owner I want to be able to approve job ads before they are posted to the job board.

(23) As the site owner I want to be able to revoke approval for a job ad if a jobseeker user has reported it for a legitimate reason, so that malicious posts are removed promptly.

(24) As the site owner I want users to feedback about any problems on the site so that any bugs/issues can be addressed promptly.

## Design

#### Fonts

Roboto mono was chosen as the main font for this website because of its readability and because of its similarity to fonts used in IDEs. This gives the site the feeling that it is a place that invites developers to interact with the site and contribute to the community. [Google Fonts](https://fonts.google.com/specimen/Roboto+Mono?query=roboto) were used to import Roboto mono to the site.

#### Colours

[Coolors.co](https://coolors.co/104f55-32746d-f4d8cd-01200f-011502 ) was used to generate the color palate of the site. The dark and light green combination was chosen because, coupled with roboto mono, the light-coloured text on the dark green background emulates a development terminal.


### Wireframes

<details>
    <summary>Small - Mobile</summary>

<details>
    <summary>Authentication</summary>
    <img src="docs/wireframes/login-phone.png" alt="wireframe for login page">
</details>
<details>
    <summary>Homepage</summary>
    <img src="docs/wireframes/home-phone.png" alt="wireframe for home page">
</details>
<details>
    <summary>Homepage sidenav</summary>
    <img src="docs/wireframes/sidenav.png" alt="wireframe for menu sidenav">
</details>
<details>
    <summary>Blog list</summary>
    <img src="docs/wireframes/blog-list-phone.png" alt="wireframe for blogs page">
</details>
<details>
    <summary>Candidate list</summary>
    <img src="docs/wireframes/candidates-phone.png" alt="wireframe for candidates page">
</details>    
<details>
    <summary>Job form</summary>
    <img src="docs/wireframes/create-job-phone.png" alt="wireframe for job form page">
</details>
<details>
    <summary>Profile form</summary>
    <img src="docs/wireframes/profile-form-phone.png" alt="wireframe for profile form page">
</details>
<details>
    <summary>Blog form</summary>
    <img src="docs/wireframes/blog-form-phone.png" alt="wireframe for blog form page">
</details>
<details>
    <summary>Job details</summary>
    <img src="docs/wireframes/job-phone.png" alt="wireframe for job detail page">
</details>
<details>
    <summary>Profile details</summary>
    <img src="docs/wireframes/profile-phone.png" alt="wireframe for profile detail page">
</details>
<details>
    <summary>Blog details</summary>
    <img src="docs/wireframes/blog-phone.png" alt="wireframe for blog detail page">
</details>
<details>
    <summary>Error pages</summary>
    <img src="docs/wireframes/404-phone.png" alt="wireframe for 404 page">
</details>

</details>

<details>
    <summary>Medium - Tablet</summary>

<details>
    <summary>Authentication</summary>
    <img src="docs/wireframes/login-tab.png" alt="wireframe for login page">
</details>
<details>
    <summary>Homepage</summary>
    <img src="docs/wireframes/home-tablet.png" alt="wireframe for home page">
</details>
<details>
    <summary>Homepage sidenav</summary>
    <img src="docs/wireframes/sidenav.png" alt="wireframe for menu sidenav">
</details>
<details>
    <summary>Blog list</summary>
    <img src="docs/wireframes/blog-list-tab.png" alt="wireframe for blogs page">
</details>
<details>
    <summary>Candidate list</summary>
    <img src="docs/wireframes/candidates-tab.png" alt="wireframe for candidates page">
</details>
<details>
    <summary>Job form</summary>
    <img src="docs/wireframes/create-job-tab.png" alt="wireframe for job form page">
</details>
<details>
    <summary>Profile form</summary>
    <img src="docs/wireframes/profile-form-tab.png" alt="wireframe for profile form page">
</details>
<details>
    <summary>Blog form</summary>
    <img src="docs/wireframes/blog-form-tab.png" alt="wireframe for blog form page">
</details>
<details>
    <summary>Job details</summary>
    <img src="docs/wireframes/job-tablet.png" alt="wireframe for job detail page">
</details>
<details>
    <summary>Profile details</summary>
    <img src="docs/wireframes/profile-tab.png" alt="wireframe for profile detail page">
</details>
<details>
    <summary>Blog details</summary>
    <img src="docs/wireframes/blog-tab.png" alt="wireframe for blog detail page">
</details>
<details>
    <summary>Error pages</summary>
    <img src="docs/wireframes/404-tab.png" alt="wireframe for 404 page">
</details>

</details>

<details>
    <summary>Large - Desktop</summary>

<details>
    <summary>Authentication</summary>
    <img src="docs/wireframes/login.png" alt="wireframe for login page">
</details>
<details>
    <summary>Homepage</summary>
    <img src="docs/wireframes/home-desktop.png" alt="wireframe for home page">
</details>
<details>
    <summary>Blog list</summary>
    <img src="docs/wireframes/blog-list-desktop.png" alt="wireframe for blogs page">
</details>
<details>
    <summary>Candidate list</summary>
    <img src="docs/wireframes/candidates-desktop.png" alt="wireframe for candidates page">
</details>
<details>
    <summary>Job form</summary>
    <img src="docs/wireframes/create-job-desktop.png" alt="wireframe for job form page">
</details>
<details>
    <summary>Profile form</summary>
    <img src="docs/wireframes/profile-form-desktop.png" alt="wireframe for profile form page">
</details>
<details>
    <summary>Blog form</summary>
    <img src="docs/wireframes/blog-form-desktop.png" alt="wireframe for blog form page">
</details>
<details>
    <summary>Job details</summary>
    <img src="docs/wireframes/job-desktop.png" alt="wireframe for job detail page">
</details>
<details>
    <summary>Profile details</summary>
    <img src="docs/wireframes/profile-desktop.png" alt="wireframe for profile detail page">
</details>
<details>
    <summary>Blog details</summary>
    <img src="docs/wireframes/blog-desktop.png" alt="wireframe for blog detail page">
</details>
<details>
    <summary>Error pages</summary>
    <img src="docs/wireframes/404-desktop.png" alt="wireframe for 404 page">
</details>

</details>

## Agile workflow

An agile methodology was employed for this project. Epics were created and each user story was assigned to an epic. Development of the project was organised into iterations where certain features were implemented to their completion before reviewing the backlog and re-assigning tasks for the next iteration.

This was achieved and tracked using the github issues/projects/kanban board features.

Any bugs found in the development process were also logged here and dealt with as backlog tasks.

### User stories

User stories and bug reports were uploaded to the project using Github issues templates. User stories were ranked with one of the following labels:

* Must have
* Should have
* Could have
* Wont have (decision made that the feature is not needed and improving other features is higher priority with remaining time)

These categories were used to prioritise the workload.

### Epics

5 epics were created using Github milestones and the user stories (uploaded as issues in the project).

<img src="docs/epics.png" alt="a screenshot of the project kanban board">

The fifth epic for the news aggregation feed was categorised entirely as 'could have'. Towards the end of the development of other features, it became apparent that this needed to be moved to the 'wont have' category in order to maximise quality of the other features.

### Kanban board

GitHub Kanban boards were used to track the progress of development:

<img src="docs/kanban.png" alt="a screenshot of the project kanban board">

## Technical Design

### Database Schema

A relational database schema was created using [Lucidchart](https://lucid.app/) to visualise the relationships between different collections of data.

<details>
    <summary>Diagram</summary>
    <p>Database for Devs & Roles:</p>
    <img src="docs/database/dbschema.png" alt="A screenshot of the database for the site">
</details><br>

### Data Models

* Django models were used to represent the tables specified in the technical design of the backend.
* Data points are represented as attributes of the model (inheriting from django's model class).

## Features

The website has fourteen pages and a variety of CRUD functionalites. Users are able to access a limited number of features without signing up. Different pages are accessbile to registered users depending on what their job-seeker/recruiter settings are toggled to on their profile.

### App Features:

<details>
    <summary>Home page</summary>
    <p>This is what the user sees upon loading the site. It contains a paginated list of job ads on the site. Any user (authenticated or not) has access to this page.</p>
    <ul>
        <li>
            <p>Home page with job postings</p>
        </li>
        <li>
            <img src="docs/features/signup.png" alt="A screenshot of the home page">
        </li>
        <li>
            <p>Job details when clicking on a job posting</p>
        </li>
        <li>
            <img src="docs/features/signup.png" alt="A screenshot of a job detail page">
        </li>
        <li>
            <p>navigator to get the next items</p>
        </li>
        <li>
            <img src="docs/features/signup.png" alt="A screenshot of the bottom nav element">
        </li>
    </ul>
</details><br>

### Feature ideas for future development

In future the website could be further developed and improved to offer more
features and feedback to users. Some ideas include:

* A functioning smtp to run password reset emails, and other notifications to users in the case of applications being made/responded to.
* A news aggregation page that uses the mediastack API to scrape tech news and display it in a paginated list of news articles on the site.
* Modifying the job application model, and wiring up another media hosting service, so that users can upload a pdf CV/resume, and recruiters can download it when reviewing applications.
  
## Technologies Used

### Languages used

* Python
* HTML
* CSS
* JavaScript

### Other tools/websites/libraries used
* [Lucidchart](https://lucid.app/) was used to create wireframes.
* [Git](https://git-scm.com/) was used for version control.
* [GitHub](https://github.com/) was used for saving and storing files.
* [Codeanywhere](https://app.codeanywhere.com/) was the IDE used for writing and editing code.
* [Heroku](https://id.heroku.com/) was used as the hosting platform for this site.
* [amiresponsive](https://ui.dev/amiresponsive?url=https://jeremyhsimons.github.io/CI_PP2_SavvySaver/) was used to test the website across different screens and generate the picture in the [Design](#design) section.

#### 3rd party Python Libraries used

## Deployment & Local Development

The website was deployed to [Heroku](https://id.heroku.com/) using the following process:
1. Login or create an account at [Heroku](https://dashboard.heroku.com/)
<img src="docs/heroku/heroku1.png">
1. Click on New > Create new app in the top right of the screen.
<img src="docs/heroku/heroku2.png">
1. Add an app name and select location, then click 'create app'.
<img src="docs/heroku/heroku3.png">
1. Under the deploy tab of the next page, select connect to GitHub.
1. Log in to your GitHub account when prompted.
<img src="docs/heroku/heroku4.png">
1. Select the repository that you want to be connected to the Heroku app.
<img src="docs/heroku/heroku5.png">
1. Click on the settings tab.
<img src="docs/heroku/heroku6.png">
1. Scroll down to the config vars section, and add 2 config vars:
    * The first key is CREDS and the value here is the creds.json file that was generated for the google sheets API to work properly.
    * The second key is PORT and the Value is 8000
<img src="docs/heroku/heroku7.png">
1. Once you have set up the config vars, scroll down to buildpacks (still under the settings tab)
1. Add the Python and Node.js buildpacks to your app and make sure that when they are displayed, they appear in the order:
    * Python
    * Node.JS
<img src="docs/heroku/heroku8.png">
1. Navigate back to the settings tab.
1. Select automatic deploys to allow Heroku to build the site with new changes each time changes are pushed to GitHub.
<img src="docs/heroku/heroku9.png">
1. In the 'manual deploy' section beneath this, make sure the branch selected is 'main' and click deploy branch.
<img src="docs/heroku/heroku10.png">
1. The site should now be built and Heroku should provide a url for the built site.

This repository can be forked using the following process:
1. On the repository's page, go to the top-right of the page underneath the dark ribbon.
1. Click on the fork button
1. You can now work on a fork of this project. 

This repository can be cloned using the following process:
1. Go to this repository's page on GitHub.
1. Click on the code button (not the one in the navbar, but the one right above the file list).
1. Select an option, HTTPS, SSH, GitHub CLI.
1. Copy the url below to your clipboard.
1. Open Git Bash/your IDE terminal.
1. Ensure the directory you are working in is the correct one you want to paste the project into.
1. Type the command '$ git clone'
1. Paste the URL of the repository after this.
1. Hit enter on your keyboard and the project will be cloned.
 
## Testing
### Debugging
The site was tested using the following browsers:
* Google Chrome
* Mozilla Firefox
* Microsoft Edge

The site was tested on the following devices:
* Lenovo Ideapad 520S (Windows 10)
* Huawei PSmart 2019 (EMUI version 12.0.0)

### Validation

#### PEP8 Python Validator (from Code Institute)

Code institute's own Python Linter [pep8](https://pep8ci.herokuapp.com/) was used to validate all Python code in this project.

All code passed with no errors apart from the run.py file where the line limit of 80 characters had to be exceeded to display the title. These were the only errors that were found in this file.

### Manual Testing

|User story|Feature|Test|Expected Result|Actual Result|
|---|---|---|---|---|
| 1. Sign up as a new player | Sign-up prompt | When prompted by the opening view of the game, answer 'n', enter new details and type 'enter' | Program accepts/signs user up. | Works as expected. |

<details>
    <summary>Screenshots</summary>
    <img src="" alt="A screenshot of the sign up prompt."><br>
</details><br>


### Automated Testing
Unit test suites were written for all the models.py, forms.py, and views.py of each app within this django project.

<details>
    <summary>Screenshots</summary>

</details><br>

### Bugs

The following bugs were documented during the development of this project:

* User object does not have userprofile attribute
<details>
<summary>screenshot:</summary>
<img src="docs/bugs/bug1.png" alt="a screenshot of bug 1">
</details>

* Materialize Checkboxes not displaying properly
<details>
<summary>screenshot:</summary>
<img src="docs/bugs/bug2.png" alt="a screenshot of bug 2">
</details>

* Submitting form to create a user profile resulted in a database error.
<details>
<summary>screenshot:</summary>
<img src="docs/bugs/bug3.png" alt="a screenshot of bug 3">
</details>

* Textarea fields in all forms are too short (vertically)
<details>
<summary>screenshot:</summary>
<img src="docs/bugs/bug4.png" alt="a screenshot of bug 4">
</details>

* Materialize Crispy Form rendering of image fields caused visual bugs with labels
<details>
<summary>screenshot:</summary>
<img src="docs/bugs/bug5.png" alt="a screenshot of bug 5">
</details>

The following issues remain unfixed, and as a consequence the features were removed so as to maintain a strong user experience without error messages to interrupt it.

* Sending reset password request results in 504 error
<details>
<summary>screenshot:</summary>
<img src="docs/bugs/bugnotfixed1.png" alt="a screenshot of bugnotfixed1">
</details>

* Cannot access uploaded pdf cv file from job application.
<details>
<summary>screenshot:</summary>
<img src="docs/bugs/bugnotfixed2.png" alt="a screenshot of bugnotfixed2">
</details>

## Credits

### 3rd party code used

#### 3rd party Python libraries/modules

#### Code found online when solving bugs in own code.
* credits to the CI team for the code used to fetch/display git hub profile information

### Acknowledgements

* Thanks to my Mentor Mo Shami for his immensely valuable feedback, advice and encouragement throughout this project. Thanks for pushing me to do the best I can!
* Thanks to the CI tutors for all their help with bugs that I couldn't get my head round! Thanks also for helping me out when Codeanywhere did weird things and required extra adjustment!
* Thanks for the CI slack community for all your valuable input and help bugfixing!
* Thanks to the wonderful CI London Community for all the moral support!.
* Thanks to Oli for his user acceptance tesing and feedback. Cheers for breaking my site...