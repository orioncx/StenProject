# -*- encoding: utf8 -*-
from django.db import models
from tinymce.models import HTMLField
from filebrowser.fields import FileBrowseField


# Create your models here.
class FlatFeatures(models.Model):
    name = models.CharField(max_length=31, verbose_name=u'Обозначение')

    def __unicode__(self):
        return self.name or ''


class Flat(models.Model):
    title = models.CharField(null=True, blank=True, max_length=255, verbose_name=u'Заголовок')
    slug = models.SlugField(null=True, blank=True, max_length=255, verbose_name=u'Адрес страницы')
    adress = models.CharField(max_length=255, null=True, blank=True, verbose_name=u'Адрес')
    image = FileBrowseField("Image", max_length=200, blank=True, null=True)
    description = HTMLField(null=True, blank=True, verbose_name=u'Описание')
    coords = models.CharField(null=True, blank=True, max_length=31, verbose_name=u'Координаты', help_text='52.44167,30.98333')
    rooms = models.IntegerField(null=True, blank=True, verbose_name=u'Количество комнат')

    features = models.ManyToManyField(FlatFeatures, null=True, blank=True, verbose_name=u'Фишки')

    def __unicode__(self):
        return self.adress or u''


class FlatPhoto(models.Model):
    flat = models.ForeignKey(Flat, verbose_name=u'Квартира')
    image = FileBrowseField("Image", max_length=200, blank=True, null=True)
    title = models.CharField(max_length=128, verbose_name=u'Заголовок', blank=True, null=True)
    description = models.CharField(max_length=128, verbose_name=u'Описание', blank=True, null=True)

    def __unicode__(self):
        return self.title or u''
