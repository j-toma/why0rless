# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0027_auto_20171014_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='lesson_title',
            field=models.CharField(default='Default Lesson Title', max_length=60),
        ),
        migrations.AlterField(
            model_name='homework',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 17, 5, 9, 15, 228234, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='session',
            name='day',
            field=models.DateField(default=datetime.date(2017, 10, 15)),
        ),
    ]
