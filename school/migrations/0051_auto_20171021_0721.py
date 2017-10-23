# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0050_auto_20171021_0713'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='profile',
            field=models.ForeignKey(default=0, to='school.UserProfile'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='homework',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 23, 7, 21, 20, 636079, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='profile',
            field=models.ForeignKey(default=1, to='school.UserProfile'),
            preserve_default=False,
        ),
    ]
