from django.urls import path
from . import views

urlpatterns = [
    path('base/', views.basehtmlrender),
    path('register/', views.registration, name='register'),
    path('Login/', views.Login, name='Login'),
    path('DisplayDetails/', views.sendDetailsToUser, name='Display'),
    path('SearchDetails/', views.GetDetailsFromUSer, name='Search'),
    path('Profile/',views.profile, name='profile')

]