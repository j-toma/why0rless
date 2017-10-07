# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

#from .models import Course, Student, Teacher, Homework, Session
from .models import *


admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Homework)
admin.site.register(Vocabulary)
admin.site.register(Session)
admin.site.register(Content)
#admin.site.register(Grade)
admin.site.register(Attendance)
