from django.conf.urls import url 
from . import views 

urlpatterns = [
  url(r'^$', views.index, name='index'),
#  url(r'^(?P<course_id>[0-9]+)/course/$', views.index, name='course_detail'),
]
