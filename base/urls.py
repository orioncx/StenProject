from django.conf.urls import url
from base.views import FlatDetailView, FlatListView

urlpatterns = [
    url(r'^flat/(?P<slug>[\w-]+)/$', FlatDetailView.as_view(),
        name='flat_detail'),
    url(r'^$', FlatListView.as_view(),
        name='flat_list'),
]
