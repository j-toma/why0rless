# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

from .models import *


def index(request):
    course_list = Course.objects.all()[:10]
    student_list = Student.objects.all()[:10]
    teacher_list = Teacher.objects.all()[:10]
    homework_list = Homework.objects.all()[:10]
    template = loader.get_template('school/index.html')
    context = {
        'course_list': course_list,
        'student_list': student_list,
        'teacher_list': teacher_list,
        'homework_list': homework_list,
    }
    return HttpResponse(template.render(context, request))

#    return HttpResponse("Hello, world. You're at the school index.")

#def course_detail(request, course_id):
#    return HttpResponse("You're looking at %s" % course_id)
