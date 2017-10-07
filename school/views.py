# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import UpdateView, CreateView, DeleteView, ListView
from django.core.urlresolvers import reverse_lazy, reverse, resolve
from django.shortcuts import render
from django.db import transaction
from django.http import HttpResponse
from django.template import loader

from .models import *
from .forms import *


def index(request):
    course_list = Course.objects.all()
    student_list = Student.objects.all()
    teacher_list = Teacher.objects.all()
    homework_list = Homework.objects.all()
    vocabulary_list = Vocabulary.objects.all()
    session_list = Session.objects.all()
    template = loader.get_template('school/index.html')
    context = {
        'course_list': course_list,
        'student_list': student_list,
        'teacher_list': teacher_list,
        'homework_list': homework_list,
        'vocabulary_list': vocabulary_list,
        'session_list': session_list,
    }
    return HttpResponse(template.render(context, request))

#    return HttpResponse("Hello, world. You're at the school index.")

def course_view(request, course_id):
    course = Course.objects.get(pk=course_id)
    return render(request, 'school/course_view.html', {'course':course})
#   return HttpResponse("You're looking at %s" % course_id)

def teacher_view(request, teacher_id):
    teacher = Teacher.objects.get(pk=teacher_id)
    return render(request, 'school/teacher_view.html', {'teacher':teacher})

def student_view(request, student_id):
    student = Student.objects.get(pk=student_id)
    return render(request, 'school/student_view.html', {'student':student})

#class StudentList(ListView):
#    model = Student
class AttendanceList(ListView):
    model = Attendance

class StudentAttendanceNoteCreate(CreateView):
#    model = Student
#    fields = ['english_name']
#    success_url = reverse_lazy('student-list') #should this be changed to session view?   
    model = Attendance
    fields = ['attendend', 'was_late']
    success_url = reverse_lazy('attendance_list')#want this to be session view

    def get_context_data(self, **kwargs):
        data = super(StudentAttendanceNoteCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['attendancenotes'] = AttendanceNoteFormSet(self.request.POST)
        else:
            data['attendancenotes'] = AttendanceNoteFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        attendancenotes = context['attendancenotes']
        with transaction.atomic():
            self.object = form.save()
            if attendancenotes.is_valid():
                attendancenotes.instance = self.object
                attendancenotes.save()
        return super(StudentAttendanceNoteCreate, self).form_valid(form)  

#class StudentUpdate(UpdateView):
#    model = Student
#    success_url = '/'
#    fields = ['first_name', 'last_name']
class AttendanceUpdate(UpdateView):
    model = Attendance
    success_url = '/'
    fields = ['attended','was_late']

class StudentAttendanceNoteUpdate(UpdateView):
#    model = Student
#    fields = ['english_name']
#    success_url = reverse_lazy('student-list') #should this be changed to session view?   
    model = Attendance
    fields = ['attended','was_late']
    success_url = reverse_lazy('attendance_list')#or 'student-list', but should eventually be 'session_view'

    def get_context_data(self, **kwargs):
        data = super(StudentAttendanceNoteUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['attendancenotes'] = AttendanceNoteFormSet(self.request.POST, instance=self.object)
        else:
            data['attendancenotes'] = AttendanceNoteFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        attendancenotes = context['attendancenotes']
        with transaction.atomic():
            self.object = form.save()
            if attendancenotes.is_valid():
                attendancenotes.instance = self.object
                attendancenotes.save()
        return super(StudentAttendanceNoteUpdate, self).form_valid(form)  

#class StudentDelete(DeleteView):
#    model = Student
#    success_url = reverse_lazy('student-list') 
class AttendanceDelete(DeleteView):
    model = Student
    success_url = reverse_lazy('session_view')

def homework_view(request, homework_id):
    homework = Homework.objects.get(pk=homework_id)
    return render(request, 'school/homework_view.html', {'homework':homework})

def vocabulary_view(request, vocabulary_id):
    vocabulary = Vocabulary.objects.get(pk=vocabulary_id)
    return render(request, 'school/vocabulary_view.html', {'vocabulary':vocabulary})

def session_view(request, session_id):
    session = Session.objects.get(pk=session_id)
    return render(request, 'school/session_view.html', {'session':session})

def attendance_view(request, attendance_id):
    attendance = Attendance.objects.get(pk=attendance_id)
    return render(request, 'school/attendance_view.html', {'attendance':attendance})

class HomeworkCreate(CreateView):
    model = Homework
    fields = '__all__'
    template_name_suffix = '_create'
    success_url = reverse_lazy('index')

class HomeworkUpdate(UpdateView):
    model = Homework
    fields = '__all__'
    template_name_suffix = '_create'
    success_url = reverse_lazy('index')

class HomeworkDelete(DeleteView):
    model = Homework
#    template_name_suffix = '_delete'
    success_url = reverse_lazy('index')

#class VocabularyCreate(CreateView):
#    model = Vocabulary

#class AttendanceFormUpdate(UpdateView):
#    model = Attendance
#    fields = ['attendend', 'was_late']
#    success_url = reverse_lazy('index')
#    
#    def get_content_data(self, **kwargs):
#        data = super(AttendanceFormUpdate, self).get_content_data(**kwargs)
#        if self.request.POST:
#            data['attendanceforms'] = AttendanceFormSet(self.request.POST, instance=self.object)
#        else:
#            data['attendanceforms'] = AttendanceFormSet(instance=self.object)
#        return data
#
#    def form_valid(self, form):
#        context = self.get_context_data()
#        attendanceforms = context['attendanceforms']
#        with transaction.atomic():
#            self.object = form.save()
#            if attendanceforms.is_valid():
#                attendanceforms.instance = self.object
#                attendanceforms.save()
#        return super(AttendanceFormUpdate, self).form_valid(form)  

def edit_attendance(request, attendance_id):
    attendance = Attendance.objects.get(pk=attendance_id) 
    if request.method == 'POST':
        form = AttendanceForm(request.POST,instance=attendance)
        if form.is_valid():
            form.save()
    else:
        form = AttendanceForm()
    return render(request, 'school/edit_attendance.html',{'form':form, 'attendance':attendance})
    



