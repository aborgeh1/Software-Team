from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registration, name='index'),
    path('Login/', views.Login, name='index'),
    path('sendDetails/', views.sendDetails, name='index'),
    path('getDetails/', views.getDetails, name='index'),

]