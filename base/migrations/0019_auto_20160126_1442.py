# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_auto_20160124_1319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='price_byr',
            field=models.CharField(max_length=63, null=True, verbose_name='\u0426\u0435\u043d\u0430 \u0432 \u0431\u0435\u043b\u043a\u0430\u0445', blank=True),
        ),
        migrations.AlterField(
            model_name='flat',
            name='price_usd',
            field=models.CharField(max_length=63, null=True, verbose_name='\u0426\u0435\u043d\u0430 \u0432 \u0434\u043e\u043b\u043b\u0430\u0440\u0430\u0445', blank=True),
        ),
    ]
