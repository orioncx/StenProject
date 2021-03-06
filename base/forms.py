__author__ = 'orion'
from base.models import Feedback
from django.forms import ModelForm


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'rate', 'country', 'text']
