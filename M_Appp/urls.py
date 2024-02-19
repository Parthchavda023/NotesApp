from django.contrib import admin
from django.urls import path
from M_Appp import views

urlpatterns = [
    path('', views.index),
    path('notes/', views.notes, name='notes'),
    path('about/', views.about),
    path('contact/', views.contact),
    path('logout/', views.userlogout),
    path('update/', views.profile_update),
]
