
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello/<str:username>', views.hello ),
    path('about/', views.about, name='about' ),
    path('projects/', views.projects, name='projects' ),
    path('tasks/', views.tasks, name='tasks' ),
    path('create_tasks/', views.createTask, name='createTask' ),
    path('create_projects/', views.createProject, name='createProject' ),
]