import json
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import TemplateView, ListView
from base.models import Flat, FlatPhoto


class FlatDetailView(TemplateView):
    template_name = 'flat_detail.html'

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
        context['photos'] = json.dumps(galery_photos)
        context['flat'] = flat
        return context


class FlatListView(ListView):
    model = Flat
    template_name = 'flat_list.html'
