# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0013_auto_20171010_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(to='school.Student'),
        ),
        migrations.AlterField(
            model_name='homework',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 12, 7, 2, 25, 954105, tzinfo=utc)),
        ),
    ]
