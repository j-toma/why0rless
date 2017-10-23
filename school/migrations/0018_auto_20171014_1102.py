# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0017_auto_20171010_0827'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='notes',
        ),
        migrations.AlterField(
            model_name='attendance',
            name='note',
            field=models.CharField(default='Nothing to say', max_length=255),
        ),
        migrations.AlterField(
            model_name='homework',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 16, 11, 2, 4, 45701, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='session',
            name='day',
            field=models.DateField(default=datetime.date(2017, 10, 14)),
        ),
    ]
