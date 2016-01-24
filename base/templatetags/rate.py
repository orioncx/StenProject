# -*- encoding: utf-8 -*-
from django import template
register = template.Library()


@register.inclusion_tag('inclusion/rate.html')
def stars(rate):
    return {
        "rate": u'★'*rate+u'☆'*(5-rate)
    }
