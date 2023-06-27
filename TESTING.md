## Browser/Device Compatibility
The site was tested using the following browsers:
* Google Chrome
* Mozilla Firefox
* Microsoft Edge

The site was tested on the following devices:
* Lenovo Ideapad 520S (Windows 10)
* Huawei PSmart 2019 (EMUI version 12.0.0)

## Manual Testing

|User story|Feature|Test|Expected Result|Actual Result|
|---|---|---|---|---|
| 1. Sign up as a new user | Sign-up page | Clicking on register, entering details into the form, clicking submit | Site gives feedback to say registration is successful. | Works as expected. |

<details>
    <summary>Screenshots</summary>
    <img src="" alt="A screenshot of the sign up prompt."><br>
</details><br>

|User story|Feature|Test|Expected Result|Actual Result|
|---|---|---|---|---|
| 2. View paginated list of jobs | Home page | entering the url of the site into browser, hitting enter. | To be taken straight away to a list of jobs which I can click on and see the details. | Works as expected. |

|User story|Feature|Test|Expected Result|Actual Result|
|---|---|---|---|---|
| 3. Create a profile for employers to find out more about me. | Create profile page | After signing up as a new user, get redirected to create profile page. Fill out the form with valid data and click submit. | When 'view profile' is now clicked in the navbar, user should see their profile details displayed correctly. | Works as expected. |

|User story|Feature|Test|Expected Result|Actual Result|
|---|---|---|---|---|
| 4. Easily navigate between site features. | Navbar | From the 'view profile' page, click on the home button to return to perusing the job ads. | To be redirected back to the home page with the job ads. | Works as expected. |

|User story|Feature|Test|Expected Result|Actual Result|
|---|---|---|---|---|
| 5. See jobs already applied for. | Track applications page | (as an authorised job-seeker) From the home page, click on the 'track application' button to see jobs applied for. | To see a list of jobs I've made applications to. clicking on one will take the user to the details of the job. | Works as expected. |

|User story|Feature|Test|Expected Result|Actual Result|
|---|---|---|---|---|
| 6. Apply for a job. | Create Application page | (as an authorised job-seeker) From the home page, click on a job to access the details. scroll down to the apply button and click it. Fill out the form that follows with valid data and click submit. | To see that an application for this job has appeared in my 'track applications page'. |

|User story|Feature|Test|Expected Result|Actual Result|
|---|---|---|---|---|
| 7. See how many applicants there are for a job. | Job detail page. | From the home page, click on a job to access the details. scroll down to the bottom of the page. | To see the number of applicants that there are for this job. |

|User story|Feature|Test|Expected Result|Actual Result|
|---|---|---|---|---|
| 8. Withdraw application. | Job detail page. | (as an authorised job-seeker) From the home page, click n the 'track applications' page and click the 'withdraw application button and click 'delete' at the following modal. | From the admin panel, view the job applications list and see that the application is no longer there. |

|User story|Feature|Test|Expected Result|Actual Result|
|---|---|---|---|---|
| 9. Withdraw application. | Job detail page. | (as an authorised job-seeker) From the home page, click n the 'track applications' page and click the 'withdraw application button and click 'delete' at the following modal. | From the admin panel, view the job applications list and see that the application is no longer there. |

## Automated Testing

### Automated Testing
Unit test suites were written for all the models.py, forms.py, and views.py of each app within this django project. the coverage library was used to measure the percentage of python code tested for each app. the results for each test suite, and each app's coverage are below.

<details>
    <summary>Screenshots</summary>

</details><br>