# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20160122_0847'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='slug_en',
            field=models.SlugField(max_length=255, null=True, verbose_name='\u0410\u0434\u0440\u0435\u0441 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b', blank=True),
        ),
        migrations.AddField(
            model_name='flat',
            name='slug_ru',
            field=models.SlugField(max_length=255, null=True, verbose_name='\u0410\u0434\u0440\u0435\u0441 \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u044b', blank=True),
        ),
    ]
