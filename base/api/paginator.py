from django.http import HttpResponse
from django.template.loader import render_to_string
from base.models import Feedback, Flat
from django.shortcuts import render
from django.core.paginator import Paginator


def get_paginated_feedbacks(request, per_page=2, page=None, flat_id=None):
    if not page:
        page=1
    flat = None
    if flat_id:
        flat = Flat.objects.get(pk=flat_id)
    if flat:
        feedbacks = Feedback.objects.filter(flat=flat, approved=True).order_by('-created_at')
    else:
        feedbacks = Feedback.objects.filter(approved=True).order_by('-created_at')
    paginator = Paginator(feedbacks, per_page)
    feedbacks = paginator.page(page)
    show_pagination = len(paginator.page_range) > 1
    return render_to_string('inclusion/feedbacks.html', {'feedbacks': feedbacks, 'paginator': paginator, "flat": flat,'show_pagination':show_pagination})


def paginator_view(request):
    flat_id = request.GET.get('flat', None)
    page = request.GET.get('page', None)
    return HttpResponse(get_paginated_feedbacks(request, page=page, flat_id=flat_id))
