# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView, ListView
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy, reverse, resolve
from django.shortcuts import render, get_object_or_404, redirect
from django.db import transaction
from django.http import HttpResponse
from django.template import loader
from datetime import timedelta
from django.utils import timezone

from .models import *
from .forms import *

def index(request):
    course_list = Course.objects.all()
    student_list = Student.objects.all()
    teacher_list = Teacher.objects.all()
    staff_list = Staff.objects.all()
    homework_list = Homework.objects.all()
    vocabulary_list = Vocabulary.objects.all()
    session_list = Session.objects.all()
    template = loader.get_template('school/index.html')
    context = {
        'course_list': course_list,
        'student_list': student_list,
        'teacher_list': teacher_list,
        'staff_list': staff_list,
        'homework_list': homework_list,
        'vocabulary_list': vocabulary_list,
        'session_list': session_list,
    }
    return HttpResponse(template.render(context, request))

#    return HttpResponse("Hello, world. You're at the school index.")

def course_view(request, course_id):
    course = Course.objects.get(pk=course_id)
    sessions = Session.objects.filter(course=course)
    registered_students = course.students.all()
    return render(request, 'school/course_view.html', {'course':course,'sessions':sessions,'registered_students':registered_students})
#   return HttpResponse("You're looking at %s" % course_id)

def staff_view(request, staff_id):
    staff = Staff.objects.get(pk=staff_id)
    return render(request, 'school/staff_view.html', {'staff': staff})

def create_user_student(request, staff_id):
    staff = get_object_or_404(Staff, pk=staff_id)
    user_form = UserForm(request.POST or None) 
    if user_form.is_valid():
        new_user = User.objects.create_user(**user_form.cleaned_data) 
        new_user.save()
        #new_user.profile = user.profile
        new_user.profile.created_by = staff
        new_user.save()
        return render(request,'school/user_created_student.html',{'user':new_user})
    return render(request, 'school/user_create_student.html',{'form':user_form})

def create_user_teacher(request, staff_id):
    staff = get_object_or_404(Staff, pk=staff_id)
    user_form = UserForm(request.POST or None) 
    if user_form.is_valid():
        new_user = User.objects.create_user(**user_form.cleaned_data) 
        new_user.save()
        #new_user.profile = user.profile
        new_user.profile.created_by = staff
        new_user.save()
        return render(request,'school/user_created_teacher.html',{'user':new_user})
    return render(request, 'school/user_create_teacher.html',{'form':user_form})

def created_user_student(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'school/user_created_student.html',{'user':user})
def created_user_teacher(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'school/user_created_teacher.html',{'user':user})
    

#    if request.method == "POST":
#        form = UserForm(request.POST)
#        if form.is_valid():
#            new_user = User.objects.create_user(**form.cleaned_data)
#            username = new_user.username
#            new_user.save()
#            
#            return render(request, 'school/student_create.html' , {'username':username})
#    success_url = 'index'
#def created_user(request, s

def create_student(request,user_id):
#def create_student(request):
    user = User.objects.get(pk=user_id)
    student_form = StudentForm(request.POST or None)
    if student_form.is_valid():
        new_student = student_form.save(commit=False)
        new_student.profile = user.profile
        new_student.save()
        return render(request,'school/student_view.html', {'student':new_student})
    return render(request,'school/student_create.html', {'form':student_form})
    
    #success_url = reverse_lazy('session_view',args=session_id)

def create_course(request,staff_id):
    staff = get_object_or_404(Staff, pk=staff_id)
    course_form = CourseForm(request.POST or None)
    if course_form.is_valid():
        new_course = course_form.save(commit=False)
        #new_course.created_by = staff
        new_course.save()
        return render(request, 'school/course_view.html', {'course':new_course})
    return render(request, 'school/course_create.html', {'form':course_form}) 

def create_teacher(request,user_id):
#def create_student(request):
    user = User.objects.get(pk=user_id)
    teacher_form = TeacherForm(request.POST or None)
    if teacher_form.is_valid():
        new_teacher = teacher_form.save(commit=False)
        new_teacher.profile = user.profile
        new_teacher.save()
        return render(request,'school/teacher_view.html', {'teacher':new_teacher})
    return render(request,'school/teacher_create.html', {'form':teacher_form})

def teacher_view(request, teacher_id):
    teacher = Teacher.objects.get(pk=teacher_id)
    sessions = Session.objects.filter(teacher=teacher,day__gte=timezone.now()-timedelta(days=5))
    return render(request, 'school/teacher_view.html', {'teacher':teacher,'sessions':sessions})


def student_view(request, student_id):
    student = Student.objects.get(pk=student_id)

    courses = student.course_set.all()
    courses_with_sessions = [course for course in courses if len(course.course_sessions.all()) >0]
    latest_sessions = [ Session.objects.filter(course=c).latest('day') for c in courses_with_sessions ]
#    sessions = student.session_set.filter(day__gte=timezone.now()-timedelta(days=2))

    sessions_with_vocab = [session for session in latest_sessions]
    vocabulary = [', '.join([str(word.word) for word in session.vocabulary.all()]) for session in sessions_with_vocab]

    latest_sessions_content = [session.content.all() for session in latest_sessions ]
    content = [ str(content[0].lesson_title) if len(content)>0 else 'No content' for content in latest_sessions_content] #note that this just takes lesson title from first content of each session 
   
    session_hw_list = [session.homework.all() for session in latest_sessions]
    homework= [str(homework[0].assignment_name) if len(homework)>0 else 'No homework' for homework in session_hw_list] #again only gets from first one
#    data = {'sessions':latest_sessions,'content':content,'homework':homework,'vocabulary':vocabulary}
    data = [latest_sessions,content,homework,vocabulary]
    formatted_data = [ [ l[i] for l in data ] for i in range(len(data[0])) ] 
    return render(request, 'school/student_view.html', {'student':student,'courses':courses,'data':formatted_data})

#    return render(request, 'school/student_view.html', {'student':student,'courses':courses,'sessions':latest_sessions,'vocabulary':vocabulary})
#class StudentList(ListView):
#    model = Student
#class AttendanceList(ListView):
#    model = Attendance
   # will probably use session_view instead of this listview #
   # on second thought might need to test that the management form can handle the booleanfield first -- loooks like it can :) # 


#class StudentAttendanceNoteCreate(CreateView):
##    model = Student
##    fields = ['english_name']
##    success_url = reverse_lazy('student-list') #should this be changed to session view?   
#    model = Attendance
##    fields = ['attendend', 'was_late']
#    fields = []
#    success_url = reverse_lazy('attendance_list')#want this to be session view
#
#    def get_context_data(self, **kwargs):
#        data = super(StudentAttendanceNoteCreate, self).get_context_data(**kwargs)
#        if self.request.POST:
#            data['attendancenotes'] = AttendanceNoteFormSet(self.request.POST)
#        else:
#            data['attendancenotes'] = AttendanceNoteFormSet()
#        return data
#
#    def form_valid(self, form):
#        context = self.get_context_data()
#        attendancenotes = context['attendancenotes']
#        with transaction.atomic():
#            self.object = form.save()
#            if attendancenotes.is_valid():
#                attendancenotes.instance = self.object
#                attendancenotes.save()
#        return super(StudentAttendanceNoteCreate, self).form_valid(form)  

#class StudentUpdate(UpdateView):
#    model = Student
#    success_url = '/'
#    fields = ['first_name', 'last_name']
#class AttendanceUpdate(UpdateView):
#    model = Attendance
#    success_url = '/'
##    fields = ['attended','was_late']
#    fields = []
#
#class StudentAttendanceNoteUpdate(UpdateView):
##    model = Student
##    fields = ['english_name']
##    success_url = reverse_lazy('student-list') #should this be changed to session view?   
#    model = Attendance
##    fields = ['attended','was_late']
#    fields = []
#    success_url = reverse_lazy('attendance_list')#or 'student-list', but should eventually be 'session_view'
#
#    def get_context_data(self, **kwargs):
#        data = super(StudentAttendanceNoteUpdate, self).get_context_data(**kwargs)
#        if self.request.POST:
#            data['attendancenotes'] = AttendanceNoteFormSet(self.request.POST, instance=self.object)
#        else:
#            data['attendancenotes'] = AttendanceNoteFormSet(instance=self.object)
#        return data
#
#    def form_valid(self, form):
#        context = self.get_context_data()
#        attendancenotes = context['attendancenotes']
#        with transaction.atomic():
#            self.object = form.save()
#            if attendancenotes.is_valid():
#                attendancenotes.instance = self.object
#                attendancenotes.save()
#        return super(StudentAttendanceNoteUpdate, self).form_valid(form)  

#class StudentDelete(DeleteView):
#    model = Student
#    success_url = reverse_lazy('student-list') 

def homework_view(request, homework_id):
    homework = Homework.objects.get(pk=homework_id)
    return render(request, 'school/homework_view.html', {'homework':homework})

def vocabulary_view(request, vocabulary_id):
    vocabulary = Vocabulary.objects.get(pk=vocabulary_id)
    return render(request, 'school/vocabulary_view.html', {'vocabulary':vocabulary})

def session_view(request, session_id):
    session = Session.objects.get(pk=session_id)
    return render(request, 'school/session_view.html', {'session':session})

def content_view(request, content_id):
    content = Content.objects.get(pk=content_id)
    return render(request, 'school/content_view.html', {'content':content})
#def sess(request, form_class=SearchForm):
#    queryset = Session.objects.all()
#    search_form = SearchForm(request.REQUEST)
#    if search_form.is_valid():
#        course = search_form.cleaned_data.get('course',None)
#        if course:
#            queryset = queryset.filter(course__icontains=course) 
#    return object_list(request,
#                       queryset = queryset,
#                       template_name = "school/sesslist_view.html",
#                       extra_context = {'search_form': search_form},
#                       paginate_by = 200,
#                       page = request.GET.get('page',1)
#                      )

class SessionList(ListView):
    model = Session

#class SessionCreate(CreateView):
#    model = Session
#    fields = '__all__'
#    form = SessionForm(request.POST, course=request.course) 

#class SessionUpdate(UpdateView):
#    model = Session
#    field = ['teacher','course','day','week']
#    success_url = '/'

#class SessionCreate(CreateView):
#    model = Session
#    fields = ['teacher','day']
#    
#    #success_url = reverse_lazy('session_list')
#    
#    def get_success_url(self):
#        return reverse_lazy('course_view',args=(self.object.course.pk,))   
#    def get_context_data(self, **kwargs):
#        data = super(SessionCreate, self).get_context_data(**kwargs)
#        if self.request.POST:
#            data['session'] = SessionCreate()
#        else:
#            data['session'] = SessionCreate()
#        return data
#    def form_valid(self,form):
#        context = self.get_context_data()
#        session = context['session']
#        with transaction.atomic():
#            self.object = form.save()
#            if session.is_valid():
#                session.instance = self.object
#                session.course = Course.objects.get(pk=self.kwargs.get('pk'))
#                session.save()
#        return super(SessionCreate, self).form_valid(form)
def create_session(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    session_form = SessionForm(request.POST or None)
    if session_form.is_valid():
        new_session = session_form.save(commit=False)
        new_session.course = course
        new_session.teacher = course.teacher
        new_session.save() 

        #registered_students = self.object.course.students.all() 
        registered_students = course.students.all()
        attendance_list = [ Attendance(session=new_session,student=s) for s in registered_students]
        Attendance.objects.bulk_create(attendance_list)

        return render(request,'school/session_view.html',{'session':new_session})
    
    return render(request,'school/session_form.html',{'form':session_form})
#    def form_valid(self, form):
#        response = super(SessionCreate, self).form_valid(form)
#        registered_students = self.object.course.students.all() 
#        attendance_list = [ Attendance(session=self.object,student=s) for s in registered_students]
#        Attendance.objects.bulk_create(attendance_list)
#        return response
        
#    def get_context_data(self, **kwargs):
#        data = super(AttendanceFormCreate, self).get_context_data(**kwargs)
#        if self.request.POST:
#            data['attendance'] = AttendanceFormSet(self.request.POST)
#        else:
#            data['attendance'] = AttendanceFormSet()
#        return data
##    
##    def generate_attendance(self):
##        sess = self.object
##        registered_students = sess.course.students.all()
##        attendance_list = [Attendance(session=sess,student=s) for s in registered_students]
##        Attendance.objects.bulk_create(attendance_list)
#
#    def form_valid(self, form):
#        context = self.get_context_data()
#        attendance = context['attendance']
#        with transaction.atomic():
#            self.object = form.save()

#
#            if attendance.is_valid():
#                attendance.instance = self.object
#                attendance.save()
#        return super(AttendanceFormCreate, self).form_valid(form)

class SessionAttendanceUpdate(UpdateView):
    model = Session
    fields = []
    #success_url = reverse_lazy('session_view') 
 
    def get_success_url(self):
        return reverse_lazy('session_view',args=(self.object.pk,))
    
    def get_context_data(self, **kwargs):
        data = super(SessionAttendanceUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['attendance'] = AttendanceFormSet(self.request.POST, instance=self.object)
        else:
            data['attendance'] = AttendanceFormSet(instance=self.object)
        return data
    
    def form_valid(self, form):
        context = self.get_context_data()
        attendance = context['attendance']
        with transaction.atomic():
            self.object = form.save()
            if attendance.is_valid():
                attendance.instance = self.object
                attendance.save()
        return super(SessionAttendanceUpdate, self).form_valid(form)

class SessionDelete(DeleteView):
    model = Session
    #success_url = reverse_lazy('session_list')

    def get_success_url(self):
        return reverse_lazy('course_view', args=(self.object.course.pk,))

def attendance_view(request, attendance_id):
    attendance = Attendance.objects.get(pk=attendance_id)
    return render(request, 'school/attendance_view.html', {'attendance':attendance})

# do i need the base class to have DetailView for slug to work?
#class SessionDetailView(DetailView):
#    model=Session 


#class VocabularyCreate(CreateView):
#    model = Vocabulary
#    fields = ['word','definition','example','translation']
##    form_class = VocabularyForm
#    template_name_suffix = '_create'
#
##    def get_success_url(self):
##        return reverse_lazy('session_view',args=self.object.session.pk,) 
#
##    def form_valid(self, form):
##        form.instance.session = get_object_or_404(Session,pk=self.kwargs['session_id'])
##        return super(VocabularyForm, self).form_valid(form)
##    def form_valid(self, form):
##        form.instance.session_id = self.kwargs.get('pk')
##        return super(VocabularyCreate, self).form_valid(form)
##    fields = ['word','definition','example','translation']
#    #form_class = VocabularyForm   
##    
#    def get_initial(self):
#        session = get_object_or_404(Session, slug=self.kwargs.get('slug'))
#        return {
#            'session':session,
#        }

def create_vocabulary(request, session_id):
    session = get_object_or_404(Session, pk=session_id)
    vocabulary_form = VocabularyForm(request.POST or None)
    if vocabulary_form.is_valid():
        new_word = vocabulary_form.save(commit=False)
        new_word.session = session
        new_word.save()
        return render(request,'school/vocabulary_view.html',{'vocabulary':new_word})
    
    #success_url = reverse_lazy('session_view',args=session_id)

    return render(request, 'school/vocabulary_create.html', {'form':vocabulary_form})
#    def form_valid(self, form): 
#        vocabulary = form.save(commit=False)
#        session_id = form.data['session_id']
#        session = get_object_or404(Session, id=session_id)
#        vocabulary.session = session
#        return super(VocabularyCreate, self).form_valid(form)
#    
#    def get_context_data(self, **kwargs):
#        context = super(VocabularyCreate, self).get_context_data(**kwargs)
#        context['s_id'] = self.kwargs['session_id']
#        return context

class VocabularyUpdate(UpdateView):
    model = Vocabulary
    fields = ['word','definition','translation','example']
    template_name_suffix = '_create'
#    success_url = reverse_lazy('index')
    def get_success_url(self):
        return reverse_lazy('session_view',args=(self.object.session.pk,))


class VocabularyDelete(DeleteView):
    model = Vocabulary
#    template_name_suffix = '_delete'
#    success_url = reverse_lazy('index')
    def get_success_url(self):
        return reverse_lazy('session_view',args=(self.object.session.pk,))

#class ContentCreate(CreateView):
#    model = Content
#    fields = ['course','session','lesson_title','lesson_plan']
#    template_name_suffix = '_create'
#
#    def get_success_url(self):
#        return reverse_lazy('session_view',args=(self.object.session.pk,))
def create_content(request, session_id):
    session = get_object_or_404(Session, pk=session_id)
    content_form = ContentForm(request.POST or None)
    if content_form.is_valid():
        new_content = content_form.save(commit=False)
        new_content.session = session
        new_content.save()
        return render(request,'school/content_view.html',{'content':new_content})
    
    return render(request, 'school/content_create.html', {'form':content_form})

class ContentUpdate(UpdateView):
    model = Content
    fields = ['lesson_title','lesson_plan']
    template_name_suffix = '_create'

    def get_success_url(self):
        return reverse_lazy('session_view',args=(self.object.session.pk,))

class ContentDelete(DeleteView):
    model = Content
    
    def get_success_url(self):
        return reverse_lazy('session_view',args=(self.object.session.pk,))

#class HomeworkCreate(CreateView):
#    model = Homework
##    fields = '__all__'
#    fields = '__all__'
#    template_name_suffix = '_create'
##    success_url = reverse_lazy('index')
#    def get_success_url(self):
#        return reverse_lazy('session_view',args=(self.object.session.pk,))

   
def create_homework(request, session_id):
    session = get_object_or_404(Session, pk=session_id)
    homework_form = HomeworkForm(request.POST or None)
    if homework_form.is_valid():
        new_homework = homework_form.save(commit=False)
        new_homework.session = session
        new_homework.save()
        return render(request,'school/homework_view.html',{'homework':new_homework})
    
    return render(request, 'school/homework_create.html', {'form':homework_form})

class HomeworkUpdate(UpdateView):
    model = Homework
    fields = ['assignment_name','description','due_date']
    template_name_suffix = '_create'
#   success_url = reverse_lazy('index')
    def get_success_url(self):
        return reverse_lazy('session_view',args=(self.object.session.pk,))


class HomeworkDelete(DeleteView):
    model = Homework
#    template_name_suffix = '_delete'
#    success_url = reverse_lazy('index')
    def get_success_url(self):
        return reverse_lazy('session_view',args=(self.object.session.pk,))


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

#def edit_attendance(request, attendance_id):
#    attendance = Attendance.objects.get(pk=attendance_id) 
#    if request.method == 'POST':
#        form = AttendanceForm(request.POST,instance=attendance)
#        if form.is_valid():
#            form.save()
#    else:
#        form = AttendanceForm()
#    return render(request, 'school/edit_attendance.html',{'form':form, 'attendance':attendance})
#    
#


