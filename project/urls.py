from django.conf.urls import url, include
from django.urls import path

from .views import all_projects, project_detail

urlpatterns = [
    path('',  all_projects, name="projects-view"),
    path(r'^detail/(?P<pk>\d+)/$', project_detail, name="project-detail"),
    ]
