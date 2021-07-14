"""todowoo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup', views.signupuser, name='signupuser'),
    path('', views.dashboard, name='todo'),
    path('login', views.loginuser, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('todo', views.todo_view, name='todo_view'),
    path('add-todo/', views.add_todo, name='add_todo_view'),
    path('completed-todo/', views.completed_todo_view, name='completed_todo_view'),
    path('upcoming-todo/', views.upcoming_todo_view, name='upcoming_todo_view'),
    path('late-todo/', views.late_todo_view, name='late_todo_view'),
    path('settings/', views.settings_view, name='settings'),

]
