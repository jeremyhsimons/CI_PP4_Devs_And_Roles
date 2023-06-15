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

### Front End Libraries
The [Materialize](https://materializecss.com/) CSS and JavaScript library was used to create the layout of the front end. The classes included in this library were used to make the site fully responsive and also to provide satisfying feedback to users regarding their actions.

* The grid system (rows and columns) was used to generate the layout of job postings, blog posts, and candidate list on the site.
* In conjunction with the [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) library, Materialize forms were used to generate clean and attractive form fields.
* Materialize 'modals' and 'toasts' were used to defensively programme delete functionality in the site. These features provide users with adequate notification of the consequences of their actions without redirecting them unnecessarily to extra pages.

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
<hr/>

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
<hr/>

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
<hr/>

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
* For this project, all tables' primary keys are the default django ids for object instances.

#### User model

* This was made using the django allauth library. This library handles all authentication out of the box. From the user it takes a username, email and password.

#### Contact Message model
* This includes the user who sent the contact message to the site owner as a foreign key.
* The read attribute is only used by the site admin to toggle messages they have read, and filter them out from the admin panel.

| Key | Name | Type | Validation |
|---|---|---|---|
|  | full_name | char | max_length=200, blank=False |
|  | email | email | max_length=200, blank=False |
| fk | user | User | on_delete=models.CASCADE, null=True, |
|  | date_sent | DateTime | Validation |
|  | message | Textfield | blank=False |
|  | read | bool | default=False |

#### Blog model

* User (author) is a foreign key in the blog model.
* If an instance is deleted, all related comments will also be deleted.
* Approved and reported attributes appear on several models in this site. They all serve the same purpose - for the admin to filter by approved/not approved and by reported/not reported, so that they can add or remove content from the site as is necessary.

| Key | Name | Type | Validation |
|---|---|---|---|
|  | title | char | max_length=200, unique=True |
| fk | posted_by | User | on_delete=models.CASCADE |
|  | slug | char | max_length=200, unique=True |
|  | content | text |  |
|  | summary | text |  |
|  | featured_image | cloudinary | 'image', default='placeholder' |
|  | created_on | datetime | auto_now_add=True |
|  | approved | bool | default=True |
|  | reported | bool | default=False |

#### Comment model

* Related blog post is a foreign key in the comment model.  

| Key | Name | Type | Validation |
|---|---|---|---|
|  | name | char | max_length=80 |
|  | body | text |  |
| fk | blog_post | BlogPost obj | on_delete=models.CASCADE |
|  | created_on | datetime | auto_now_add=True |
|  | approved | bool | default=True |
|  | reported | bool | default=False |

#### Job posting model

* User (job post author) is a foreign key of the job post model. This takes all the data required for a user to post/view a job ad on the site.
* If an instance is deleted, all related applications will also be deleted.
* Job postings are not approved by default. They must be verified by site admin before they make it to the site/user. This is done to protect users from potentially malicious spam or fraudulent job postings.
* text fields in the job posting model must be unique. This is done defensively to stop recruiters spamming the site with duplicate job ads which may crowd out other recruiters' ads. It makes sure everyone's ads gets a fair shot at being seen.

| Key | Name | Type | Validation |
|---|---|---|---|
|  | title | char | max_length=200, unique=False |
| fk | posted_by | User | on_delete=models.CASCADE |
|  | salary | int |  |
|  | location | char | max_length=200 |
|  | closing_date | datetime |  |
|  | featured_image | cloudinary | 'image', default='placeholder' |
|  | created_on | datetime | auto_now_add=True |
|  | company_overview | text | unique=True |
|  | job_description | text | unique=True |
|  | requirements | text | unique=True |
|  | benefits | text | unique=True |
|  | applicants | int | default=0 |
|  | approved | bool | default=False |
|  | reported | bool | default=False |

#### Job application model

* User (appplicant) and the job posting are both foreign keys. This takes all the data required for a user to apply/view an application on the site.

| Key | Name | Type | Validation |
|---|---|---|---|
| fk | candidate | User | on_delete=models.CASCADE |
| fk | job_posting | JobPosting | on_delete=models.CASCADE |
|  | created_on | datetime | auto_now_add=True |
|  | full_name | char | max_length=200 |
|  | email | email | max_length=200 |
|  | phone | int |  |
|  | linkedin | char | max_length=200 |
|  | github_username | char | max_length=200 |
|  | why_company | text | max_length=2000 |
|  | why_role | text | max_length=2000 |
|  | why_you | text | max_length=2000 |

#### User profile model

* Has a one-to-one relationship with the Allauth user model
* If deleted, the user essentially deletes their account (or makes it inactive according to Django).

| Key | Name | Type | Validation |
|---|---|---|---|
| fk | user | One-to-one field | on_delete=models.CASCADE |
|  | created_on | datetime | auto_now_add=True |
|  | first_name | char | max_length=200, blank=True |
|  | last_name | char | max_length=200, blank=True |
|  | linkedin | char | max_length=200, blank=True |
|  | github_username | char | max_length=200, blank=True |
|  | job_seeker | bool | default=False |
|  | recruiter | bool | default=False |
|  | location | char | max_length=200, blank=True |
|  | years_experience | int | null=True |
|  | education | text | blank=True |
|  | work_experience | text | blank=True |
|  | interests | text | blank=True |
|  | roles_open_to | char | max_length=200, blank=True |
|  | approved | bool | default=True |
|  | reported | bool | default=False |

#### message model

* user profile model (message recipient) is a foregin key in the message mode.
* This represents the many-to-one relationship between a profile and messages sent to it.

| Key | Name | Type | Validation |
|---|---|---|---|
| fk | recipient | User | on_delete=models.CASCADE |
|  | sent_on | datetime | auto_now_add=True |
|  | first_name | char | max_length=80, blank=False |
|  | last_name | char | max_length=80, blank=False |
|  | message | text | blank=False |
|  | email | email | blank=False |

## Features

The website has 20 pages (including error pages) and a variety of CRUD functionalites. Users are able to access a limited number of features without signing up. Different pages are accessbile to registered users depending on what their job-seeker/recruiter settings are toggled to on their profile.

### Pre-authentication:

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

<details>
    <summary>Job detail page</summary>
</details>

<details>
    <summary>Sign up/Log in</summary>
</details>

<details>
    <summary>Sign out</summary>
</details>

### Job Seeker Authentication

<details>
    <summary>Create Profile</summary>
</details>

<details>
    <summary>View Own Profile</summary>
</details>

<details>
    <summary>Edit profile details</summary>
</details>

<details>
    <summary>Delete Profile</summary>
</details>

<details>
    <summary>Job application page</summary>
</details>

<details>
    <summary>View applications</summary>
</details>

<details>
    <summary>Withdraw applications</summary>
</details>

### Recruiter Authentication

<details>
    <summary>Create job posting page</summary>
</details>

<details>
    <summary>Update job posting page</summary>
</details>

<details>
    <summary>Delete job posting</summary>
</details>

<details>
    <summary>View Candidates</summary>
</details>

<details>
    <summary>Message Candidates</summary>
</details>

### Admin Authentication

<details>
    <summary>Approve jobs/revoke approval</summary>
</details>

<details>
    <summary>View contact messages from users.</summary>
</details>

### Features available to all authenticated users

<details>
    <summary>Create blog post</summary>
</details>

<details>
    <summary>View blog post</summary>
</details>

<details>
    <summary>Update blog post</summary>
</details>

<details>
    <summary>Delete blog post</summary>
</details>

<details>
    <summary>Comment on blog post</summary>
</details>

<details>
    <summary>Delete comment</summary>
</details>

<details>
    <summary>Submit a contact form to site admin</summary>
</details>

### Feature ideas for future development

In future the website could be further developed and improved to offer more
features and feedback to users. Some ideas include:

* A functioning smtp to run password reset emails, and other notifications to users in the case of applications being made/responded to.
* A news aggregation page that uses the mediastack API to scrape tech news and display it in a paginated list of news articles on the site.
* Modifying the job application model, and wiring up another media hosting service, so that users can upload a pdf CV/resume, and recruiters can download it when reviewing applications.
* Exploring LinkedIn API to auto display candidate profiles from their provided linkedin urls
* Exploring DWP APIs to direct job-seeking users to apply for UK universal credit if they are eligible.
  
## Technologies Used

### Languages used

* Python
* HTML
* CSS
* JavaScript

### Frameworks/3rd party Libraries used for Python, CSS, JS

* [Django]() for building the MVT architecture of the site.
* [Django Summernote]() for implementing a text editor in the admin panel
* [Cloudinary]() for hosting static files.
* [Django Crispy Forms]() for rendering/formatting forms in django templates
* [Django Allauth]() for handling all user authentication features in the site.
* [Coverage] for displaying the extent of python unit testing un django apps.
* [Materialize CSS]() for frontend design/layout/responsiveness.

### Other tools/websites/libraries used
* [Figma] for creating site witeframes.
* [Favicon.io] for designing and creating site favicon.
* [Coolors.co] for selecting the site colour palate.
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

## Validation

### HTML

### CSS

### Accessibility (WAVE)

### Performance (Lighthouse)

### JavaScript

### PEP8 Python Validator (from Code Institute)

Code institute's own Python Linter [pep8](https://pep8ci.herokuapp.com/) was used to validate all Python code in this project.

All code passed with no errors.

## Bugs

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
* The code for the GitHub 

#### 3rd party Python libraries/modules

#### Code found online when solving bugs in own code.
* credits to the CI team for the code used to fetch/display git hub profile information

### Acknowledgements

* Thanks to my Mentor Mo Shami for his immensely valuable feedback, advice and encouragement throughout this project. Thanks for pushing me to do the best I can!
* Thanks to the CI tutors for all their help with bugs that I couldn't get my head round! Thanks also for helping me out when Codeanywhere did weird things and required extra adjustment!
* Thanks for the CI slack community for all your valuable input and help bugfixing!
* Thanks to the wonderful CI London Community for all the moral support!.
* Thanks to Oli for his user acceptance tesing and feedback. Cheers for breaking my site...