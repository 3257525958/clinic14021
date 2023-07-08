from django.urls import path

from reserv_app import views

urlpatterns = [
    path('',views.reservdef),
    ]
