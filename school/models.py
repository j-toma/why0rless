#+ -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime, timedelta, date
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models
from django.db.models.signals import post_save
#from django.dispatch import receiver
from django.forms import ModelForm


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    created_by = models.CharField(max_length=100, default='jtoma')

    def __str__(self):
        return 'Profile of user: {}'.format(self.user.username)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)

class Staff(models.Model):
    profile = models.OneToOneField(UserProfile)
    english_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.english_name

class Teacher(models.Model):
    profile = models.OneToOneField(UserProfile)
    english_name = models.CharField(max_length=100)   
    created_date = models.DateTimeField(default=timezone.now)
 
    def __str__(self):
        return self.english_name

class Student(models.Model):
    profile = models.OneToOneField(UserProfile)
    english_name = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    GROUPS = ['G10-C1','G10-C2','G10-C3','Diogo','G11-C1','G11-C2','G11-C3','G12-A','G12-B1','G12-B2','G12-C','G12-D']
    GROUP_CHOICES = [ (GROUPS[i],GROUPS[i]) for i in range(len(GROUPS)) ]
    class_group = models.CharField(max_length=40, choices=GROUP_CHOICES,default='G10-C1')
#    courses = models.ManyToManyField(Course)  
#    favorite_animal = models.CharField(max_length=100, default='dog')

   
    def __str__(self):
        return self.english_name


class Course(models.Model):
  course_title = models.CharField(max_length=200)   
  created_by = models.OneToOneField(Staff, related_name='creator', null=True)
  teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
  students = models.ManyToManyField(Student)
  semester = models.CharField(max_length=40, default='Fall')
  year = models.IntegerField(default=2017)
  class_group = models.CharField(max_length=40, default='')

  def __str__(self):
      return self.course_title

#class Grade(models.Model):
#    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_grade')
#    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grade')
#    grade_in_course = models.CharField(max_length=1,default='A')    

#class SessionManager(models.Manager):
#    def create_session(self, course, day):
#        
#        session = self.create(course=course, day=day)
#        registered_students = session.course.students.all()
#        attendance_list = [ Attendance(session=session,student=s) for s in registered_students ]
#        Attendance.objects.bulk_create(attendance_list)
#        return session


class Session(models.Model):
    # need to write student search, add (mark as attending), delete
    # students = models.ManyToManyField(Student, through='Attendance')
    teacher = models.ForeignKey(Teacher, related_name='teacher', null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_sessions')
    day = models.DateField(default=date.today())
    # content = models.TextField()
    #week = models.IntegerField(default=6)
    # number of class periods
    # notes = models.TextField(null=True)  
    #slug = models.SlugField(max_length=80,unique=True)
 
#    objects = SessionManager()

    def __str__(self):
        s = str(self.day) + ' ' + self.course.course_title
        return s

    def get_fields(self):
        return [field.name for field in Session._meta.fields]
   
    #def get_absolute_url(self):
   #     return reverse('session_view',kwargs={'slug':self.slug})


#@receiver(models.signals.post_save, sender=Session)
#def execute_after_save(sender, instance, created, *args, **kwargs):
#    if created:
#        sess = Session.objects.get(pk=instance)
#        registered_students = sess.course.students.all()
#        attendance_list = [ Attendance(session=sess,student=s) for s in registered_students ]
#        Attendance.objects.bulk_create(attendance_list)
#class AttendanceManager(models.Manager):
#    def create_attendance(self, title):
#        attendance = models.


class Attendance(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    attended = models.BooleanField(default=True)
    was_late = models.BooleanField(default=False)
    
    # this marks a new idea #
    note = models.CharField(max_length=255, default='Nothing to say')
    # my idea is to link attendance directly to session so i can let user modify attendance objects on session view #

    def __str__(self):
#        s = self.student.english_name + ' -- ' + self.session.course.course_title + ' -- ' + str(self.session.day) + ' -- ' + str(self.attended)
        return self.student.english_name + ' | ' + str(self.session.day) + ' | ' + self.session.course.course_title

#    def get_fields(self):
#        return [field.name

#class AttendanceNote(models.Model):
#    student = models.ForeignKey(Student)
#    attendance = models.ForeignKey(Attendance)
#    attended = models.BooleanField()
#    was_late = models.BooleanField() 
#    note = models.CharField(max_length=255)
    
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
 
    #def get_absolute_url(self):
    #    return reverse('session_view',kwargs={'slug':self.slug})

class Homework(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_hw', null=True)
    # week = models.IntegerField()
    assignment_name = models.CharField(max_length=60, default="Default Assignment Name")
    description = models.TextField(null=True)
    session = models.ForeignKey(Session, related_name='homework', null=True)
    due_date = models.DateTimeField(default=timezone.now()+timedelta(days=2))

    def __str__(self):
        return self.description

class Content(models.Model):
    course = models.ForeignKey(Course, related_name='course_content', null=True)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='content', null=True)
    lesson_title = models.CharField(max_length=60,default="Default Lesson Title")
    lesson_plan = models.TextField(null=True)
# later may want to include some upload file here
    def __str__(self):
        return self.lesson_plan
