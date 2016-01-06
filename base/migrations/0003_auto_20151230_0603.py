# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20151228_2222'),
    ]

    operations = [
        migrations.AddField(
            model_name='flatphoto',
            name='description',
            field=models.CharField(max_length=128, null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AddField(
            model_name='flatphoto',
            name='title',
            field=models.CharField(max_length=128, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True),
        ),
    ]
