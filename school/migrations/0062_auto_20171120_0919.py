# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0061_auto_20171027_0558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homework',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 22, 9, 19, 27, 940811, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='session',
            name='day',
            field=models.DateField(default=datetime.date(2017, 11, 20)),
        ),
        migrations.AlterField(
            model_name='student',
            name='class_group',
            field=models.CharField(default='G10-C1', max_length=40, choices=[('G10-C1', 'G10-C1'), ('G10-C2', 'G10-C2'), ('G10-C3', 'G10-C3'), ('Diogo', 'Diogo'), ('G11-C1', 'G11-C1'), ('G11-C2', 'G11-C2'), ('G11-C3', 'G11-C3'), ('G12-A', 'G12-A'), ('G12-B1', 'G12-B1'), ('G12-B2', 'G12-B2'), ('G12-C', 'G12-C'), ('G12-D', 'G12-D')]),
        ),
    ]
