# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0058_auto_20171023_0336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 29, 5, 28, 36, 864761, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='session',
            name='day',
            field=models.DateField(default=datetime.date(2017, 10, 27)),
        ),
    ]
