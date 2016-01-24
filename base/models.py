# -*- encoding: utf-8 -*-
from django.db import models
from tinymce.models import HTMLField
from filebrowser.fields import FileBrowseField
from django.utils.translation import ugettext as _


# Create your models here.
class FlatFeatures(models.Model):
    name = models.CharField(max_length=31, verbose_name=_(u'Обозначение'))

    def __unicode__(self):
        return self.name or ''


class Flat(models.Model):
    title = models.CharField(null=True, blank=True, max_length=255, verbose_name=_(u'Заголовок'))
    slug = models.SlugField(null=True, blank=True, max_length=255, verbose_name=_(u'Адрес страницы'))
    price_usd = models.IntegerField(null=True)
    price_byr = models.IntegerField(null=True)
    district = models.CharField(null=True, blank=True, max_length=255, verbose_name=_(u'Район'))
    adress = models.CharField(max_length=255, null=True, blank=True, verbose_name=_(u'Адрес'))
    image = FileBrowseField("Image", max_length=200, blank=True, null=True)
    description = HTMLField(null=True, blank=True, verbose_name=_(u'Описание'))
    coords = models.CharField(null=True, blank=True, max_length=31, verbose_name=_(u'Координаты'), help_text='52.44167,30.98333')
    rooms = models.IntegerField(null=True, blank=True, verbose_name=_(u'Количество комнат'))

    features = models.ManyToManyField(FlatFeatures, null=True, blank=True, verbose_name=_(u'Фишки'))

    def __unicode__(self):
        return self.title or u''


class FlatPhoto(models.Model):
    flat = models.ForeignKey(Flat, verbose_name=_(u'Квартира'))
    image = FileBrowseField("Image", max_length=200, blank=True, null=True)
    title = models.CharField(max_length=128, verbose_name=_(u'Заголовок'), blank=True, null=True)
    description = models.CharField(max_length=128, verbose_name=_(u'Описание'), blank=True, null=True)

    def __unicode__(self):
        return self.title or u''


class Feedback(models.Model):
    flat = models.ForeignKey(Flat, verbose_name=_(u'Квартира'))
    created_at = models.DateTimeField(auto_created=True,null=True,blank=True,auto_now_add=True)
    country = models.CharField(null=True, blank=True, max_length=63)
    rate = models.IntegerField(null=True, blank=True, default=5)
    name = models.CharField(null=True, blank=True, max_length=127, verbose_name=_(u'Имя'))
    text = models.TextField(null=True, blank=True, verbose_name=_(u'Отзыв'))
    approved = models.BooleanField(default=False)

    def __unicode__(self):
        return u'%s - %s(%s)' % (self.flat, self.name, self.rate)