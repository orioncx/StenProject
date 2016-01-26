from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from base.views import FlatDetailView, FlatListView,AboutUsView, rent_form_sent

urlpatterns = [


    url(r'^about_us/$', AboutUsView.as_view(),
        name='about_us'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^rent_form/', rent_form_sent, name='rent_form')
]


