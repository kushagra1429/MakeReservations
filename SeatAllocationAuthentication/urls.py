from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.SignUp, name="SignUp"),
    path('Register/', views.Register, name='Register'),
    path('SignInAuthenticate/', views.SignInAuthenticate, name='SignInAuthenticate'),
    path('SignIn/', views.SignIn, name="SignIn"),
    path('accounts/login/', views.SignIn, name="SignIn")

    # accounts/login

]