# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_auto_20160126_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='features',
        ),
        migrations.DeleteModel(
            name='FlatFeatures',
        ),
    ]
