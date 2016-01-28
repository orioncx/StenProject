# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20160106_0745'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='adress_en',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0410\u0434\u0440\u0435\u0441', blank=True),
        ),
        migrations.AddField(
            model_name='flat',
            name='adress_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0410\u0434\u0440\u0435\u0441', blank=True),
        ),
        migrations.AddField(
            model_name='flat',
            name='description_en',
            field=tinymce.models.HTMLField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AddField(
            model_name='flat',
            name='description_ru',
            field=tinymce.models.HTMLField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AddField(
            model_name='flat',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True),
        ),
        migrations.AddField(
            model_name='flat',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True),
        ),
        migrations.AddField(
            model_name='flatphoto',
            name='description_en',
            field=models.CharField(max_length=128, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AddField(
            model_name='flatphoto',
            name='description_ru',
            field=models.CharField(max_length=128, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AddField(
            model_name='flatphoto',
            name='title_en',
            field=models.CharField(max_length=128, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True),
        ),
        migrations.AddField(
            model_name='flatphoto',
            name='title_ru',
            field=models.CharField(max_length=128, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True),
        ),
        migrations.AlterField(
            model_name='flat',
            name='features',
            field=models.ManyToManyField(to='base.FlatFeatures', null=True, verbose_name='\u0424\u0438\u0448\u043a\u0438', blank=True),
        ),
    ]
