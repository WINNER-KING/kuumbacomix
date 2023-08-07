from django.urls import path
from  import .views

urlpatterns += [
    path(r'^forgotPassword/$', forgot_password.as_view(), name='forgot_password'),
    path(r'^newPassword/$', new_Password.as_view(), name='new_password'),
    path(r'^register/$', register.as_view(), name='register'),
    path(r'^users/(?P<username>\w+)/update_password/$', update_password.as_view(), name='user_update_password'),
    path(r'^users/$', get_all_users.as_view(), name='users_get_all'),
    path(r'^users/username/(?P<username>\w+)/$', get_user_username.as_view(), name='user_get_by_username'),
    path(r'^users/email/(?P<email>\w+)/$', get_user_email.as_view(), name='user_get_by_email'),
    path(r'^users/data/$', get_user_data.as_view(), name='user_filters'),
    path(r'^users/(?P<username>\w+)/update/$', update_user.as_view(), name='user_update'),
    path(r'^users/(?P<username>\w+)/delete/$', delete_user.as_view(), name='user_delete'),
    path(r'^users/(?P<username>\w+)/roles/add/$', add_role.as_view(), name='user_roles_add'),
    path(r'^users/(?P<username>\w+)/roles/remove/$', remove_role.as_view(), name='user_roles_remove'),

    
]
