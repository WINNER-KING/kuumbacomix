from django.contrib.auth.models import User

def get_all_users():
    """
    Retourne tous les utilisateurs.

    Returns:
        QuerySet: Un ensemble de tous les utilisateurs.
    """
    return User.objects.all()
