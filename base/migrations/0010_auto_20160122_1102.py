# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_auto_20160122_0942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='slug_en',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='slug_ru',
        ),
        migrations.AddField(
            model_name='flat',
            name='district',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0420\u0430\u0439\u043e\u043d', blank=True),
        ),
        migrations.AddField(
            model_name='flat',
            name='district_en',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0420\u0430\u0439\u043e\u043d', blank=True),
        ),
        migrations.AddField(
            model_name='flat',
            name='district_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0420\u0430\u0439\u043e\u043d', blank=True),
        ),
        migrations.AddField(
            model_name='flat',
            name='price_byr',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='flat',
            name='price_usd',
            field=models.IntegerField(null=True),
        ),
    ]
