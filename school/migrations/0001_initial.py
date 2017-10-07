# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('attended', models.BooleanField(default=False)),
                ('was_late', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lesson_plan', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_title', models.CharField(max_length=200)),
                ('semester', models.CharField(default='Fall', max_length=40)),
                ('year', models.IntegerField(default=2017)),
                ('class_group', models.CharField(default='', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.TextField(null=True)),
                ('course', models.ForeignKey(related_name='course_hw', to='school.Course', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.DateField(default=datetime.date.today)),
                ('week', models.IntegerField(default=6)),
                ('notes', models.TextField(null=True)),
                ('course', models.ForeignKey(related_name='course_sessions', to='school.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('english_name', models.CharField(max_length=100)),
                ('courses', models.ManyToManyField(to='school.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('english_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vocabulary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word', models.CharField(max_length=40)),
                ('definition', models.TextField(null=True)),
                ('translation', models.CharField(max_length=50)),
                ('example', models.TextField(null=True)),
                ('fromcourse', models.ForeignKey(related_name='course_vocab', to='school.Course', null=True)),
                ('session', models.ForeignKey(related_name='vocabulary', to='school.Session', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='session',
            name='students',
            field=models.ManyToManyField(to='school.Student', through='school.Attendance'),
        ),
        migrations.AddField(
            model_name='session',
            name='teacher',
            field=models.ForeignKey(related_name='teacher', to='school.Teacher', null=True),
        ),
        migrations.AddField(
            model_name='homework',
            name='session',
            field=models.ForeignKey(related_name='homework', to='school.Session', null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(to='school.Teacher', null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='from_course',
            field=models.ForeignKey(related_name='course_content', to='school.Course', null=True),
        ),
        migrations.AddField(
            model_name='content',
            name='session',
            field=models.OneToOneField(related_name='content', null=True, to='school.Session'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='session',
            field=models.ForeignKey(to='school.Session'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(to='school.Student'),
        ),
    ]
