# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='created_at',
            field=models.DateTimeField(null=True, auto_created=True, blank=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='rate',
            field=models.FloatField(null=True),
        ),
    ]
