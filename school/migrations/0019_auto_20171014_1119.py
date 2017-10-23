# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0018_auto_20171014_1102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='students',
        ),
        migrations.AlterField(
            model_name='homework',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 16, 11, 19, 49, 628477, tzinfo=utc)),
        ),
    ]
