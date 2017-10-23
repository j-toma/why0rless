# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0010_auto_20171008_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 11, 12, 1, 30, 782926, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='session',
            name='day',
            field=models.DateField(default=datetime.date(2017, 10, 9)),
        ),
    ]
