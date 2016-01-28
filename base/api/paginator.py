from base.models import Feedback

__author__ = 'orion'
from django.core.paginator import Paginator



def get_paginated_feedbacks(request, flat=None):
    if flat:
        feedbacks = Feedback.objects.filter(flat=flat, approved=True).order_by('-created_at')
    else:
        feedbacks = Feedback.objects.filter(approved=True).order_by('-created_at')
    per_page = int(request.GET.get('per_page', 10))
    paginator = Paginator(feedbacks, per_page)

    page = request.GET.get('page')
    feedbacks = paginator.page(page)

    return feedbacks