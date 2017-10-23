# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0056_auto_20171021_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='created_by',
            field=models.OneToOneField(related_name='creator', null=True, to='school.Staff'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='created_by',
            field=models.CharField(default='jtoma', max_length=100),
        ),
        migrations.AlterField(
            model_name='homework',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 24, 11, 6, 13, 801971, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='session',
            name='day',
            field=models.DateField(default=datetime.date(2017, 10, 22)),
        ),
    ]
