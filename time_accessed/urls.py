from django.urls import path

from . import views

app_name = 'time_accessed'
urlpatterns = [
    path('', views.AccessView.as_view(), name='index'),
]