# -*- encoding: utf-8 -*-
import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, FormView
from base.api.paginator import get_paginated_feedbacks
from base.forms import FeedbackForm
from base.models import Flat, FlatPhoto, Feedback
from django.core.mail import send_mail
from django.conf import settings


def rent_form_sent(request):
    # try:
    date_from = request.POST.get('date_from')
    flat = request.POST.get('flat')
    date_to = request.POST.get('date_to')
    phone = request.POST.get('phone')
    count = request.POST.get('count')
    comment = request.POST.get('comment')
    email = request.POST.get('email')
    name = request.POST.get('name')

    msg_txt = u"""\n
        Квартира: %s \n
        с: %s \n
        по: %s \n
        человек: %s \n
        Имя: %s \n
        Email: %s \n
        телефон: %s \n
        комментарий: %s \n
        """ % (flat, date_from, date_to, count, name, email, phone, comment)

    send_mail(u'Заявка на съем квартиры', msg_txt, settings.DEFAULT_FROM_EMAIL, [settings.TO_EMAIL])
    return JsonResponse({'success': True})
    # except:
    #     pass

    # return JsonResponse({'success': False}, status=400)


class FlatDetailView(FormView):
    template_name = 'flat_detail.html'
    form_class = FeedbackForm

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
        context['rendered_feedbacks'] = get_paginated_feedbacks(self.request, flat_id=flat.pk)
        context['flat'] = flat
        context['page'] = 'flats'
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

        msg_txt = u"""\n
        Получен новый комментарий. Утвердите его в админке. \n
        >
        "%s"
        """ % feedback.text
        send_mail(u'Комментарий', msg_txt, settings.DEFAULT_FROM_EMAIL, [settings.TO_EMAIL])
        self.request.session['has_commented_%s' % flat.pk] = True
        return JsonResponse({'success': True})


class AboutUsView(TemplateView):
    template_name = 'about_us.html'


class FeedbacksView(TemplateView):
    template_name = 'feedbacks.html'

    def get_context_data(self, **kwargs):
        context = super(FeedbacksView, self).get_context_data(**kwargs)
        page = self.request.GET.get('page', None)
        feedbacks = get_paginated_feedbacks(self.request, page=page, per_page=3)
        context['page'] = 'feedbacks'
        context['feedbacks'] = feedbacks
        return context


class FlatListView(ListView):
    def get_queryset(self):
        return Flat.objects.filter(show_on_index=True)

    template_name = 'flat_list.html'
    def get_context_data(self, **kwargs):
        context = super(FlatListView, self).get_context_data(**kwargs)
        context['page'] = 'flats'
        return context
