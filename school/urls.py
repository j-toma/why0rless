from django.conf.urls import url 
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from . import views 
#from school.views import HomeworkCreate

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^course/(?P<course_id>[0-9]+)$', views.course_view, name='course_view'),
  url(r'^teacher/(?P<teacher_id>[0-9]+)$', views.teacher_view, name='teacher_view'), 
  url(r'^student/(?P<student_id>[0-9]+)$', views.student_view, name='student_view'), 
  url(r'^homework/(?P<homework_id>[0-9]+)$', views.homework_view, name='homework_view'),
  url(r'^vocabulary/(?P<vocabulary_id>[0-9]+)$', views.vocabulary_view, name='vocabulary_view'),
  url(r'^session/(?P<session_id>[0-9]+)$', views.session_view, name='session_view'),  
  url(r'^attendance/(?P<attendance_id>[0-9]+)$', views.edit_attendance, name='edit_attendance'),

  url(r'^homework/create/$', views.HomeworkCreate.as_view(), name='homework_create'), 
  url(r'^homework/(?P<pk>\d+)/update/$', views.HomeworkUpdate.as_view(), name='homework_update'),
  url(r'^homework/(?P<pk>\d+)/delete/$', views.HomeworkDelete.as_view(), name='homework_delete'), 

#  url(r'^students/$', views.StudentList.as_view(), name='student-list'),
#  url(r'^student/add/$', views.StudentAttendanceNoteCreate.as_view(), name='student-add'),
#  url(r'^student/(?P<pk>[0-9]+)/$', views.StudentAttendanceNoteUpdate.as_view(), name='student-update'),
#  url(r'^student/(?P<pk>[0-9]+)/delete/$', views.StudentDelete.as_view(), name='student-delete'),

 
  url(r'^attendance/$', views.AttendanceList.as_view(), name='attendance_list'),#ultimately want this to be session_view
  url(r'^attendance/add/$', views.StudentAttendanceNoteCreate.as_view(), name='attendance_add'),
  url(r'^attendance/(?P<pk>[0-9]+)/$', views.StudentAttendanceNoteUpdate.as_view(), name='attendance_update'),
  url(r'^attendance/(?P<pk>[0-9]+)/delete/$', views.AttendanceDelete.as_view(), name='attendance_delete'),
# last two lines need <pk> instead of <xxx_id>??? is there even a difference?

]
