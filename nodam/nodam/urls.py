"""nodam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('community/', views.community, name='community'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('smokingmap/', views.smokingmap, name='smokingmap'),
    path('clinic/', views.clinic, name='clinic'),

    path('insertform/', views.insert_form, name='insertform'),
    path('insertres/', views.insert_res),
    path('detail/<int:id>', views.detail, name='detail'),
    path('updateform/<int:id>', views.update_form, name='updateform'),
    path('updateres/', views.update_res),
    path('delete/<int:id>', views.delete),

    path('dashboard1/', views.dashboard1, name='dashboard1'),
    path('dashboard2/', views.dashboard2, name='dashboard2'),
    path('dashboard3/', views.dashboard3, name='dashboard3'),
    path('dashboard4/', views.dashboard4, name='dashboard4'),
    path('dashboard5/', views.dashboard5, name='dashboard5'),
    
]
