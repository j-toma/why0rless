# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0022_auto_20171014_1204'),
    ]

    operations = [
        migrations.RenameField(
            model_name='content',
            old_name='from_course',
            new_name='course',
        ),
        migrations.AlterField(
            model_name='attendance',
            name='attended',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='homework',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 16, 13, 38, 56, 698468, tzinfo=utc)),
        ),
    ]
