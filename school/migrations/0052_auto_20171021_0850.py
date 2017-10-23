# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0051_auto_20171021_0721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 23, 8, 50, 43, 788712, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='student',
            name='profile',
            field=models.OneToOneField(to='school.UserProfile'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='profile',
            field=models.OneToOneField(to='school.UserProfile'),
        ),
    ]
