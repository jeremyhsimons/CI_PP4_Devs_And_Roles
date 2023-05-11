from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import JobPosting


class JobPostingList(generic.ListView):
    model = JobPosting
    queryset = JobPosting.objects.filter(approved=True).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 12


class JobPostingDetail(View):

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
