import json
from django import http
from django.conf import settings
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.utils.translation import check_for_language
from django.views.generic import TemplateView, ListView, FormView
from base.forms import FeedbackForm
from base.models import Flat, FlatPhoto, Feedback
from django.db.models import Q
from django.utils import translation


class FlatDetailView(FormView):
    template_name = 'flat_detail.html'
    form_class = FeedbackForm

    # def get_success_url(self):
    #     url = reverse_lazy('flat_detail')
    #     return "%s%s/" % (url, self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(FlatDetailView, self).get_context_data(**kwargs)
        slug = self.kwargs['slug']
        flat = get_object_or_404(Flat, slug=slug)
        flat_photos = FlatPhoto.objects.filter(flat=flat)
        galery_photos = []
        for flat_photo in flat_photos:
            galery_photos.append({
                "image": flat_photo.image.original.url,
                "thumb": flat_photo.image.version_generate("small").url,
                # "big": flat_photo.image.version_generate("max").url,
                "title": flat_photo.title,
                "description": flat_photo.description
            })
        feedbacks = Feedback.objects.filter(flat=flat, approved=True).order_by('-created_at')[:15]
        context['photos'] = json.dumps(galery_photos)
        context['feedbacks'] = feedbacks
        context['flat'] = flat
        if self.request.session.get('has_commented_%s' % flat.pk, False):
            context['has_commented'] = True
        return context

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'success': False}, status=400)

    def form_valid(self, form):
        # form.send_email()
        slug = self.kwargs['slug']
        flat = get_object_or_404(Flat, slug=slug)
        feedback = form.save(commit=False)
        feedback.flat = flat
        feedback.save()
        self.request.session['has_commented_%s' % flat.pk] = True
        return JsonResponse({'success': True})

class AboutUsView(TemplateView):
    template_name = 'about_us.html'


class FlatListView(ListView):
    model = Flat
    template_name = 'flat_list.html'
