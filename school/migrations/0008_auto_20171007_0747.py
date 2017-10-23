# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0007_auto_20171006_0705'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='attended',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='was_late',
        ),
        migrations.AddField(
            model_name='attendance',
            name='note',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attendancenote',
            name='attended',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='attendancenote',
            name='was_late',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
