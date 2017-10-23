# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0008_auto_20171007_0747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendancenote',
            name='attendance',
        ),
        migrations.AddField(
            model_name='attendance',
            name='attended',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attendance',
            name='was_late',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='AttendanceNote',
        ),
    ]
