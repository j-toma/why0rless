# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0011_auto_20171009_1201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='student',
            new_name='students',
        ),
        migrations.AlterField(
            model_name='homework',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 12, 6, 33, 58, 975166, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='session',
            name='day',
            field=models.DateField(default=datetime.date(2017, 10, 10)),
        ),
    ]
