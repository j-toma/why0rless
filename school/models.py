#+ -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.utils import timezone
from django.db import models
from django.forms import ModelForm


class Teacher(models.Model):
    english_name = models.CharField(max_length=100)   
    created_date = models.DateTimeField(default=timezone.now)
 
    def __str__(self):
        return self.english_name

class Student(models.Model):
    english_name = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
#    courses = models.ManyToManyField(Course)  
#    favorite_animal = models.CharField(max_length=100, default='dog')

   
    def __str__(self):
        return self.english_name


class Course(models.Model):
  course_title = models.CharField(max_length=200)   
  teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
  student = models.ManyToManyField(Student)
  semester = models.CharField(max_length=40, default='Fall')
  year = models.IntegerField(default=2017)
  class_group = models.CharField(max_length=40, default='')

  def __str__(self):
      return self.course_title

#class Grade(models.Model):
#    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_grade')
#    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grade')
#    grade_in_course = models.CharField(max_length=1,default='A')    

class Session(models.Model):
    # need to write student search, add (mark as attending), delete
    students = models.ManyToManyField(Student, through='Attendance')
    teacher = models.ForeignKey(Teacher, related_name='teacher', null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_sessions')
    day = models.DateField(default=datetime.date.today)
    # content = models.TextField()
    week = models.IntegerField(default=6)
    # number of class periods
    notes = models.TextField(null=True)  
 
    def __str__(self):
        s = str(self.day) + ' ' + self.course.course_title
        return s

    def generate_attendance(self):
        registered_students = self.course.student.all()
        attendance_list = [ Attendance(session=self,student=s) for s in registered_students ]
        Attendance.objects.bulk_create(attendance_list)

class Attendance(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    attended = models.BooleanField()
    was_late = models.BooleanField()
    
    def __str__(self):
        s = self.student.english_name + ' -- ' + self.session.course.course_title + ' -- ' + str(self.session.day) + ' -- ' + str(self.attended)
        return s

class AttendanceNote(models.Model):
#    student = models.ForeignKey(Student)
    attendance = models.ForeignKey(Attendance)
    note = models.CharField(max_length=255)
    
class Vocabulary(models.Model):
    word = models.CharField(max_length=40)
    fromcourse = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_vocab', null=True)
    session = models.ForeignKey(Session, related_name='vocabulary', null=True)
    #week = models.IntegerField(null=True)
    definition = models.TextField(null=True)
    translation = models.CharField(max_length=50)
    example = models.TextField(null=True)
     
    def __str__(self):
        return self.word


class Homework(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_hw', null=True)
    # week = models.IntegerField()
    description = models.TextField(null=True)
    session = models.ForeignKey(Session, related_name='homework', null=True)
    # due date, assigned date

    def __str__(self):
        return self.description

class Content(models.Model):
    from_course = models.ForeignKey(Course, related_name='course_content', null=True)
    session = models.OneToOneField(Session, on_delete=models.CASCADE, related_name='content', null=True)
    lesson_plan = models.TextField(null=True)

    def __str__(self):
        return self.lesson_plan
