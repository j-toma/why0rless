# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0015_auto_20171010_0709'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='week',
        ),
        migrations.AlterField(
            model_name='homework',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 12, 7, 55, 44, 379582, tzinfo=utc)),
        ),
    ]
