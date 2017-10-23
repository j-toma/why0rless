# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0032_auto_20171015_1031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='slug',
        ),
        migrations.AlterField(
            model_name='homework',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 17, 13, 35, 16, 497158, tzinfo=utc)),
        ),
    ]
