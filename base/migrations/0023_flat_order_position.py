# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0022_flat_show_on_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='order_position',
            field=models.IntegerField(default=0, null=True, verbose_name='\u041f\u0440\u0438\u043e\u0440\u0438\u0442\u0435\u0442 \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f', blank=True),
        ),
    ]
