# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_remove_student_favorite_animal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='attended',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='was_late',
            field=models.BooleanField(),
        ),
    ]
