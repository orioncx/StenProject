# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('adress', models.CharField(max_length=255, null=True, verbose_name='\u0410\u0434\u0440\u0435\u0441', blank=True)),
                ('description', tinymce.models.HTMLField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='FlatPhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('flat', models.ForeignKey(to='base.Flat')),
            ],
        ),
    ]
