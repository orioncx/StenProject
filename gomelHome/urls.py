"""gomelHome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.core.urlresolvers import reverse, reverse_lazy
from filebrowser.sites import site
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.flatpages.sitemaps import FlatPageSitemap
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap, Sitemap
from base.models import Flat
from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from base.views import FlatDetailView, FlatListView,AboutUsView, rent_form_sent, FeedbacksView, robots


class BlogSitemap(Sitemap):
    priority = 0.5

    def items(self):
        return Flat.objects.all()

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return "/flat/%s/" % obj.slug


class StaticViewSitemap(Sitemap):
    priority = 0.6

    def items(self):
        return ['flat_list', 'about_us']

    def location(self, item):
        return reverse_lazy(item)


urlpatterns = [
                  url(r'^admin/filebrowser/', include(site.urls)),
                  url(r'^grappelli/', include('grappelli.urls')),
                  url(r'^admin/', include(admin.site.urls)),
                  url(r'^tinymce/', include('tinymce.urls')),
                  url(r'^mce_filebrowser/', include('mce_filebrowser.urls')),
                  url(r'^', include('base.urls')),
                  url(r'^rosetta/', include('rosetta.urls')),
                  url(r'^robots\.txt$', robots, name='robots'),
                  url(r'^sitemap\.xml$', sitemap,
                      {'sitemaps': {'flats': BlogSitemap(), 'static': StaticViewSitemap()}},
                      name='django.contrib.sitemaps.views.sitemap'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    url(r'^flat/(?P<slug>[\w-]+)/$', FlatDetailView.as_view(),
        name='flat_detail'),
    url(r'^flat/$', FlatDetailView.as_view(),
        name='flat_detail'),
    url(r'^$', FlatListView.as_view(),
        name='flat_list'),
    url(r'^feedbacks/$', FeedbacksView.as_view(),
        name='feedbacks_list'),
)
