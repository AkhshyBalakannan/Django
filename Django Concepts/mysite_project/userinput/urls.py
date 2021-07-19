from django.urls import include, path
from userinput import views

urlpatterns = [
    path('default/', views.defaultInput, name='default-input'),
    path('name/', views.yourname, name='your-name'),
    path('nameform/', views.get_name, name='name-form-basic'),
    path('feedback/', views.get_feedback, name='feedback'),
    path('manualfeedback/', views.get_manual_feedback, name='manual-feedback'),
    path('loopfeedback/', views.get_loop_feedback, name='loop-feedback'),
    path('', views.notFound, name='Not-Found-404'),
]
