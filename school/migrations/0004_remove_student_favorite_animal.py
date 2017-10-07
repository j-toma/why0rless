# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_student_favorite_animal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='favorite_animal',
        ),
    ]
