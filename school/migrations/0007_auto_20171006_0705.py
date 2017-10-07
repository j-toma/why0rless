# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_auto_20171004_0644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendancenote',
            name='student',
        ),
        migrations.AddField(
            model_name='attendancenote',
            name='attendance',
            field=models.ForeignKey(default=1, to='school.Attendance'),
            preserve_default=False,
        ),
    ]
