from django.shortcuts import render
from django.views import generic
from .models import JobPosting


class JobPostingList(generic.ListView):
    model = JobPosting
    queryset = JobPosting.objects.filter(approved=True).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 12
