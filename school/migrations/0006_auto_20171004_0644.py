# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_auto_20171003_0806'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceNote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('note', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='teacher',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='attendancenote',
            name='student',
            field=models.ForeignKey(to='school.Student'),
        ),
    ]
