from django.urls import path
from . import views

urlpatterns = [
  path('',                        views.home,      name = 'posts'),
  #path('home/',                   views.tulia,       name = 'home'),
  ]