from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.greetings, name='greetings'),
    path('finding/', views.finding, name='finding'),
    path('about/', views.about, name='about'),
    path('loading/', views.loading, name='loading'),
    path('admin', admin.site.urls, name='admin'),
    path('login/', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('register/', views.register, name='register'),
    path('open_doc/', views.open_doc, name='open_doc'),
    path('notes/', views.notes, name='notes'),
]
