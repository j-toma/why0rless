# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Course, Student, Teacher, Homework

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Homework)
