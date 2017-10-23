# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0028_auto_20171015_0509'),
    ]

    operations = [
        migrations.AddField(
            model_name='homework',
            name='assignment_name',
            field=models.CharField(default='Default Assignment Name', max_length=60),
        ),
        migrations.AlterField(
            model_name='homework',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 17, 5, 33, 32, 99098, tzinfo=utc)),
        ),
    ]
