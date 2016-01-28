# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_auto_20160128_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='show_on_index',
            field=models.BooleanField(default=True, verbose_name='\u041d\u0430 \u0433\u043b\u0430\u0432\u043d\u043e\u0439'),
        ),
    ]
