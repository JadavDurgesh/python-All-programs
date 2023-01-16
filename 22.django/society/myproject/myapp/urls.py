from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [

    path('', views.index, name='index'),
    path('login/', views.login, name='loginname'),
    path('logout/',views.logout, name='logout'),
    path('profile/',views.profile, name='profile'),
    path('add_member/',views.add_member,name='add_member'),
    path('change_password/',views.change_password,name='change_password'),
    path('update_profile_chairmen/',views.update_profile_chairmen,name='update_profile_chairmen'),
    path('view_member/',views.view_member ,name='view_member'),
    path('add_notice/',views.add_notice ,name='add_notice'),
    path('view_notice/',views.view_notice ,name='view_notice'),

]
