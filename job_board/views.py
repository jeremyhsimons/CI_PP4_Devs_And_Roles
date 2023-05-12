from django.shortcuts import render, get_object_or_404
from django.views import generic, View
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
