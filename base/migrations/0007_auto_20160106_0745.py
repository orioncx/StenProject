# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_auto_20160105_2131'),
    ]

    operations = [
        migrations.CreateModel(
            name='FlatFeatures',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=31, verbose_name='\u041e\u0431\u043e\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435')),
            ],
        ),
        migrations.AddField(
            model_name='flat',
            name='features',
            field=models.ManyToManyField(to='base.FlatFeatures', null=True, blank=True),
        ),
    ]
