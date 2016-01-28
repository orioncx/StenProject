# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_auto_20160122_1102'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=127, null=True, verbose_name='\u0418\u043c\u044f', blank=True)),
                ('text', models.TextField(null=True, verbose_name='\u041e\u0442\u0437\u044b\u0432', blank=True)),
                ('flat', models.ForeignKey(verbose_name='\u041a\u0432\u0430\u0440\u0442\u0438\u0440\u0430', to='base.Flat')),
            ],
        ),
    ]
