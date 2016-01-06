# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20151230_0603'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='slug',
            field=models.SlugField(max_length=255, null=True, verbose_name='\u0410\u0434\u0440\u0435\u0441 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b', blank=True),
        ),
        migrations.AddField(
            model_name='flat',
            name='title',
            field=models.CharField(max_length=255, null=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True),
        ),
    ]
