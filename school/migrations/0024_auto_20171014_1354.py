# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0023_auto_20171014_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='session',
            field=models.ForeignKey(related_name='content', to='school.Session', null=True),
        ),
        migrations.AlterField(
            model_name='homework',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 16, 13, 54, 36, 270035, tzinfo=utc)),
        ),
    ]
