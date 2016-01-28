# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_auto_20160123_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='country',
            field=models.CharField(max_length=63, null=True, blank=True),
        ),
    ]
