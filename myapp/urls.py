
from django.urls import path
from . import views

urlpatterns = [
    path('generate/', views.generate_pdf, name='generate'),
    path('pdf/', views.generate_pdf),
]