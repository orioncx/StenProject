# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_feedback_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
