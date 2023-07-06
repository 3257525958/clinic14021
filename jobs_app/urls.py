from django.urls import path

from jobs_app import views

urlpatterns = [
    path('',views.jobs),
    path('test',views.testdef),
    ]
