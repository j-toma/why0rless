# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Teacher(models.Model):
    english_name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.english_name


class Course(models.Model):
    course_title = models.CharField(max_length=200)   
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.course_title

#    class Meta:
#        ordering = ('course_title',)

class Homework(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    week = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.description


class Student(models.Model):
    english_name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course)  
   
    def __str__(self):
        return self.english_name

#    class Meta:
#        ordering = ('english_name')



