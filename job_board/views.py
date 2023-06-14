# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 3rd Party
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Internal
from .models import JobPosting, JobApplication
from .forms import JobPostingForm, JobApplicationForm


class JobPostingList(generic.ListView):
    """
    A class to view a paginated list of job postings
    on the home page.
    """
    model = JobPosting
    queryset = JobPosting.objects.filter(approved=True).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 12


class JobPostingDetail(View):
    """
    A class to view the details of an individual job posting
    that has been displayed on the site.
    """

    def get(self, request, pk, *args, **kwargs):
        queryset = JobPosting.objects.filter(approved=True)
        jobpost = get_object_or_404(queryset, pk=pk)
        applications = jobpost.job_application.order_by('-created_on')
        jobpost.applicants = applications.count()

        return render(
            request,
            "job-post-detail.html",
            {
                'jobpost': jobpost,
                'applications': applications,
            },
        )


class CreateJobPosting(generic.CreateView):
    """
    A class to view the form required to add a job
    posting to the site.
    """
    model = JobPosting
    form_class = JobPostingForm
    template_name = 'create-job-post.html'

    def post(self, request, *args, **kwargs):
        jobpost_form = JobPostingForm(request.POST, request.FILES)

        if jobpost_form.is_valid():
            jobpost_form.instance.posted_by = request.user
            messages.success(request,
                             """
                             JOB POSTING SUBMITTED SUCCESSFULLY.
                             IT WILL GO LIVE ON THE SITE FOLLOWING APPROVAL BY
                             ADMINS.
                             """)

            jobpost_form.save()
            return redirect('home')

        else:
            messages.error(request,
                           """
                           YOUR REQUEST COULD NOT BE PROCESSED.
                           PLEASE ENSURE YOU COMPLETE
                           ALL FORM FIELDS CORRECTLY.
                           """)
            return render(
                request,
                'create-job-post.html',
                {
                    'form': jobpost_form
                }
            )


class UpdateJobPosting(generic.UpdateView):
    """
    A class to handle updates to job postings.
    """
    model = JobPosting
    form_class = JobPostingForm
    template_name = 'update-job-post.html'

    def get(self, request, pk, *args, **kwargs):
        queryset = JobPosting.objects.filter(approved=True)
        jobpost = get_object_or_404(queryset, pk=pk)
        form = JobPostingForm(
            initial={
                'title': jobpost.title,
                'salary': jobpost.salary,
                'location': jobpost.location,
                'closing_date': jobpost.closing_date,
                'featured_image': jobpost.featured_image,
                'company_overview': jobpost.company_overview,
                'job_description': jobpost.job_description,
                'requirements': jobpost.requirements,
                'benefits': jobpost.benefits
            }
        )
        return render(
            request,
            'update-job-post.html',
            {
                'form': form,
                'jobpost': jobpost,
            }
        )

    def post(self, request, pk, *args, **kwargs):
        queryset = JobPosting.objects.filter(approved=True)
        jobpost = get_object_or_404(queryset, pk=pk)
        updated_form = JobPostingForm(
            request.POST, request.FILES, instance=jobpost
            )

        if updated_form.is_valid():
            updated_form.instance.posted_by = request.user
            updated_form.save()
            messages.success(request, 'JOB SUCCESSFULLY UPDATED.')
            return redirect('home')

        else:
            updated_form = JobPostingForm()
            messages.error(request, 'PLEASE SUBMIT A VALID, UPDATED FORM.')
            return render(
                request,
                'update-job-post.html',
                {
                    'form': updated_form,
                    'jobpost': jobpost,
                }
            )


@login_required
def delete_job_posting(request, jobpost_id):
    """
    View that handles deletion of
    job postings.
    """
    jobpost = get_object_or_404(JobPosting, pk=jobpost_id)
    if request.user == jobpost.posted_by:
        jobpost.delete()
        messages.success(request, 'JOB POSTING SUCCESSFULLY DELETED')
        return HttpResponseRedirect(reverse('home'))
    else:
        messages.error(request, "YOU CANNOT DELETE A POST YOU DIDN'T CREATE")
        return HttpResponseRedirect(reverse('home'))


@login_required
def report_job_posting(request, jobpost_id):
    """
    View that handles reporting of
    job postings.
    """
    jobpost = get_object_or_404(JobPosting, pk=jobpost_id)
    if jobpost.reported is False and request.user != jobpost.posted_by:
        jobpost.reported = True
        jobpost.save()
        messages.success(request, "POSTING REPORTED. AN ADMIN WILL REVIEW IT")
        return HttpResponseRedirect(reverse('home'))
    else:
        messages.error(request, "YOU CANNOT REPORT THIS JOB POSTING")
        return HttpResponseRedirect(reverse('home'))


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Views to handle all job application logic.


class ViewApplicationDetails(View):
    """
    A class to handle viewing the full data
    contained in each job application.
    """

    def get(self, request, pk, *args, **kwargs):
        application = get_object_or_404(JobApplication, pk=pk)
        jobpost = application.job_posting

        return render(
            request,
            "application-detail.html",
            {
                'application': application,
                'jobpost': jobpost,
            },
        )


class CreateJobApplication(generic.CreateView):
    """
    A class to handle users writing and submitting
    job applications.
    """
    model = JobApplication
    form_class = JobApplicationForm
    template_name = 'create-job-application.html'

    def post(self, request, job_id, *args, **kwargs):
        """
        Function to handle POST requests for submitted
        application forms.
        """
        application_form = JobApplicationForm(data=request.POST)
        job_posting = get_object_or_404(JobPosting, pk=job_id)

        if application_form.is_valid():
            application_form.instance.job_posting = job_posting
            application_form.instance.candidate = request.user
            application_form.save()
            messages.success(request, 'APPLICATION SENT SUCCESSFULLY')
            return redirect('home')

        else:
            messages.error(request, 'PLEASE SUBMIT A VALID APPLICATION FORM')
            return render(
                request,
                'create-job-application.html',
                {
                    'form': application_form,
                }
            )


class TrackMyApplications(generic.ListView):
    """
    A class-based view to display all the user's
    job applications.
    """
    model = JobApplication
    template_name = 'my_applications.html'

    def get(self, request, *args, **kwargs):
        my_applications = JobApplication.objects.filter(
            candidate=request.user).order_by('created_on')
        return render(
            request,
            'my_applications.html',
            {'applications': my_applications}
        )


@login_required
def delete_application(request, application_id):
    """
    View that handles withdrawal of
    job applications.
    """
    application = get_object_or_404(JobApplication, pk=application_id)
    if request.user == application.candidate:
        application.delete()
        messages.success(request, 'JOB POSTING SUCCESSFULLY DELETED')
        return HttpResponseRedirect(reverse('home'))
    else:
        messages.error(request, "YOU CANNOT DELETE A POST YOU DIDN'T CREATE")
        return HttpResponseRedirect(reverse('home'))
