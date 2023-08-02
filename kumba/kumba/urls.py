"""
URL configuration for kumba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib.auth.views import login, logout, forgotPassword, register

from .views.users import *

urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^forgotPassword/$', forgot_password, name='forgot_password'),
    url(r'^newPassword/$', new_Password, name='new_password'),
    url(r'^register/$', register.as_view(), name='register'),
    url(r'^users/(?P<username>\w+)/update_password/$', update_password.as_view(), name='user_update_password'),
    url(r'^users/$', get_all_users.as_view(), name='users_get_all'),
    url(r'^users/username/(?P<username>\w+)/$', get_user_username.as_view(), name='user_get_by_username'),
    url(r'^users/email/(?P<email>\w+)/$', get_user_email.as_view(), name='user_get_by_email'),
    url(r'^users/data/$', get_user_data.as_view(), name='user_filters'),
    url(r'^users/(?P<username>\w+)/update/$', update_user.as_view(), name='user_update'),
    url(r'^users/(?P<username>\w+)/delete/$', delete_user.as_view(), name='user_delete'),
    url(r'^users/(?P<username>\w+)/roles/add/$', add_role.as_view(), name='user_roles_add'),
    url(r'^users/(?P<username>\w+)/roles/remove/$', remove_role.as_view(), name='user_roles_remove'),
    
]
