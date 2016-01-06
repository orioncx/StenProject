# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20160104_1210'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='image',
            field=filebrowser.fields.FileBrowseField(max_length=200, null=True, verbose_name=b'Image', blank=True),
        ),
    ]
