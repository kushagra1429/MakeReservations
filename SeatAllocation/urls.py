from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('Bookings/', views.bookings, name='bookings'),
    path('Bookings/MyBookings/', views.MyBookings, name="MyBookings"),
    path('BookingsAdmin/MyBookings/', views.MyBookingsAdmin, name="MyBookingsAdmin"),
    path('Authenticate/', views.Authenticate, name='Authenticate'),
    path('DeleteAction/', views.DeleteAction, name='DeleteAction'),
    path('BookingsAdmin/', views.BookingsAdmin, name='BookingsAdmin'),
    path('BookingsAdmin/AllAccess', views.AllAccess, name='AllAccess'),
    path('Bookings/logoutB/', views.logoutB, name='logoutB'),
    path('BookingsAdmin/logoutB/', views.logoutB, name='logoutB'),
    path('BookingsAdmin/download/', views.download, name='download')






]
