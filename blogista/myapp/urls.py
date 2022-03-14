"""blogista URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from myapp import views

urlpatterns = [
     path('',views.index,name='index'),
     path('login/',views.user_login,name='login'),
     path('register/',views.user_register,name='register'),
     path('post_blog',views.post_blog,name='post_blog'),
     path('blog_detail/<int:id>',views.blog_detail,name='blog_detail'),
     path('logout',views.user_logout,name='logout'),
     path('delete/<int:id>',views.delete,name='delete'),
     path('edit/<int:id>',views.edit,name='edit'),
     path('change_password',views.change_password,name='change_password'),
     path('reset_password',auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'),name="reset_password"),
     path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name="password_reset_done"),
     path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name="password_reset_confirm"),
     path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name="password_reset_complete"),
] 
