from django.conf.urls import url, include
from base.api.paginator import  paginator_view
from base.views import  rent_form_sent

urlpatterns = [
    url(r'^api/feedbacks/', paginator_view, name='api_feedbacks'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^rent_form/', rent_form_sent, name='rent_form')
]
