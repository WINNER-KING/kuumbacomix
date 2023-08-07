from django.contrib.auth.models import User

def get_user_username(username):

    return User.objects.get(username=username)

def get_user_email(email):
    return User.objects.get(email=email)
