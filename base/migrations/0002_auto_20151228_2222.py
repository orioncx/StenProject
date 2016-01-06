# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flatphoto',
            name='image',
            field=filebrowser.fields.FileBrowseField(max_length=200, null=True, verbose_name=b'Image', blank=True),
        ),
        migrations.AlterField(
            model_name='flat',
            name='description',
            field=tinymce.models.HTMLField(null=True, verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435', blank=True),
        ),
        migrations.AlterField(
            model_name='flatphoto',
            name='flat',
            field=models.ForeignKey(verbose_name='\u041a\u0432\u0430\u0440\u0442\u0438\u0440\u0430', to='base.Flat'),
        ),
    ]
