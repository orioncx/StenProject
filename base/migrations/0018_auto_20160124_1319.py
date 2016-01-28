# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_auto_20160123_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 1, 24, 13, 19, 54, 51586), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='feedback',
            name='rate',
            field=models.IntegerField(default=5, null=True, blank=True),
        ),
    ]
