from django.conf.urls import url, include
from base.views import FlatDetailView, FlatListView,AboutUsView

urlpatterns = [
    url(r'^flat/(?P<slug>[\w-]+)/$', FlatDetailView.as_view(),
        name='flat_detail'),
    url(r'^flat/$', FlatDetailView.as_view(),
        name='flat_detail'),
    url(r'^$', FlatListView.as_view(),
        name='flat_list'),
    url(r'^about_us/$', AboutUsView.as_view(),
        name='about_us'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]
