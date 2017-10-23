from django.conf.urls import url, include 
from django.conf import settings
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views 
#from school.views import HomeworkCreate

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^course/(?P<course_id>[0-9]+)$', views.course_view, name='course_view'),
  url(r'^staff/(?P<staff_id>[0-9]+)$', views.staff_view, name='staff_view'),
  url(r'^teacher/(?P<teacher_id>[0-9]+)$', views.teacher_view, name='teacher_view'), 
  url(r'^student/(?P<student_id>[0-9]+)$', views.student_view, name='student_view'), 
  url(r'^homework/(?P<homework_id>[0-9]+)$', views.homework_view, name='homework_view'),
  url(r'^vocabulary/(?P<vocabulary_id>[0-9]+)$', views.vocabulary_view, name='vocabulary_view'),
  url(r'^session/(?P<session_id>[0-9]+)/$', views.session_view, name='session_view'),  
  #url(r'^session/(?P<slug>[-\w]+)$', views.session_view,name='session_view'),
  url(r'^content/(?P<content_id>[0-9]+)/$', views.content_view, name='content_view'),
#  url(r'^attendance/(?P<attendance_id>[0-9]+)$', views.edit_attendance, name='edit_attendance'),

  url(r'^staff/(?P<staff_id>\d+)/user/create/student/$', views.create_user_student, name='user_create_student'), 
  url(r'^staff/(?P<staff_id>\d+)/user/create/teacher/$', views.create_user_teacher, name='user_create_teacher'), 
  url(r'^staff/created_user_student/$', views.created_user_student, name='user_created_student'), 
  url(r'^staff/created_user_teacher/$', views.created_user_teacher, name='user_created_teacher'),

  url(r'^user/(?P<user_id>\d+)/student/create/$', views.create_student, name='student_create'),
  url(r'^user/(?P<user_id>\d+)/teacher/create/$', views.create_teacher, name='teacher_create'),

  url(r'^staff/(?P<staff_id>\d+)/course/create/$', views.create_course, name='course_create'),

  url(r'^session/(?P<session_id>[0-9]+)/vocabulary/create/$', views.create_vocabulary, name='vocabulary_create'),
#  url(r'^(?P<slug>[-\w]+)$', views.VocabularyCreate.as_view(), name='vocabulary_create'),
  url(r'^vocabulary/(?P<pk>\d+)/update/$', views.VocabularyUpdate.as_view(), name='vocabulary_update'),
  url(r'^vocabulary/(?P<pk>\d+)/delete/$', views.VocabularyDelete.as_view(), name='vocabulary_delete'),

  url(r'^session/(?P<session_id>[0-9]+)/content/create/$', views.create_content, name='content_create'),
  url(r'^content/(?P<pk>\d+)/update/$', views.ContentUpdate.as_view(), name='content_update'),
  url(r'^content/(?P<pk>\d+)/delete/$', views.ContentDelete.as_view(), name='content_delete'),

  url(r'^session/(?P<session_id>[0-9]+)/homework/create/$', views.create_homework, name='homework_create'), 
  url(r'^homework/(?P<pk>\d+)/update/$', views.HomeworkUpdate.as_view(), name='homework_update'),
  url(r'^homework/(?P<pk>\d+)/delete/$', views.HomeworkDelete.as_view(), name='homework_delete'), 


#  url(r'^students/$', views.StudentList.as_view(), name='student-list'),
#  url(r'^student/add/$', views.StudentAttendanceNoteCreate.as_view(), name='student-add'),
#  url(r'^student/(?P<pk>[0-9]+)/$', views.StudentAttendanceNoteUpdate.as_view(), name='student-update'),
#  url(r'^student/(?P<pk>[0-9]+)/delete/$', views.StudentDelete.as_view(), name='student-delete'),

 
#  url(r'^attendance/$', views.AttendanceList.as_view(), name='attendance_list'),#ultimately want this to be session_view
#  url(r'^attendance/add/$', views.StudentAttendanceNoteCreate.as_view(), name='attendance_add'),
#  url(r'^attendance/(?P<pk>[0-9]+)/$', views.StudentAttendanceNoteUpdate.as_view(), name='attendance_update'),
#  url(r'^attendance/(?P<pk>[0-9]+)/delete/$', views.AttendanceDelete.as_view(), name='attendance_delete'),
# last two lines need <pk> instead of <xxx_id>??? is there even a difference?

  # to get an attedance for for each student on session_view #
  # url is going to need a session id and an attendance id #
#  url(r'^session/(?P<session_id>[0-9]+)/attendance/create/$', views.StudentAttendanceFormCreate.as_view(), name='attendence_create') 
  # should not be any need for a list view since will use session view #
  # table is not rendering, so I am going to imitate the example exactly #
  url(r'^sessions/$', views.SessionList.as_view(), name='session_list'),
  url(r'^course/(?P<course_id>[0-9]+)/session/create/$', views.create_session, name='session_form'),  
  url(r'^session/(?P<pk>[0-9]+)/update/$', views.SessionAttendanceUpdate.as_view(), name='session_update'),
  url(r'^session/(?P<pk>[0-9]+)/delete/$', views.SessionDelete.as_view(), name='session_delete'),

  url(r'^accounts/', include('django.contrib.auth.urls')),

]  
#urlpatterns += staticfiles_urlpatterns()
#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
