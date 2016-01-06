# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_flat_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='coords',
            field=models.CharField(help_text=b'52.44167,30.98333', max_length=31, null=True, verbose_name='\u041a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b', blank=True),
        ),
        migrations.AddField(
            model_name='flat',
            name='rooms',
            field=models.IntegerField(null=True, verbose_name='\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043a\u043e\u043c\u043d\u0430\u0442', blank=True),
        ),
    ]
