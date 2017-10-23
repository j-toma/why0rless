# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0020_auto_20171014_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='class_group',
            field=models.CharField(default='G10-C1', max_length=40, choices=[(b'0', 'G10-C1'), (b'1', 'G10-C2'), (b'2', 'G10-C3'), (b'3', 'Diogo'), (b'4', 'G11-C1'), (b'5', 'G11-C2'), (b'6', 'G11-C3'), (b'7', 'G12-A'), (b'8', 'G12-B1'), (b'9', 'G12-B2'), (b'10', 'G12-C'), (b'11', 'G12-D')]),
        ),
        migrations.AlterField(
            model_name='homework',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 16, 11, 48, 4, 357055, tzinfo=utc)),
        ),
    ]
