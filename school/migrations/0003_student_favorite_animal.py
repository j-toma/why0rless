# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20171003_0257'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='favorite_animal',
            field=models.CharField(default='dog', max_length=100),
        ),
    ]
