from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import JobPosting
from .forms import JobPostingForm


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

        return render(
            request,
            "job-post-detail.html",
            {
                "jobpost": jobpost,
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
        jobpost_form = JobPostingForm(data=request.POST)

        if jobpost_form.is_valid():
            jobpost_form.instance.posted_by = request.user
            print('form saved')
            jobpost_form.save()

        else:
            print(f'form failed{jobpost_form.errors}')
            jobpost_form = JobPostingForm()

        return render(
            request,
            'create-job-post.html'
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
            {'form': form, }
        )

    def post(self, request, pk, *args, **kwargs):
        queryset = JobPosting.objects.filter(approved=True)
        jobpost = get_object_or_404(queryset, pk=pk)
        updated_form = JobPostingForm(data=request.POST, instance=jobpost)

        if updated_form.is_valid():
            updated_form.instance.posted_by = request.user
            print('form saved')
            updated_form.save()
            return render(
                request,
                'index.html'
            )

        else:
            print(f'form failed{updated_form.errors}')
            updated_form = JobPostingForm()
            return render(
                request,
                'update-job-post.html'
            )
