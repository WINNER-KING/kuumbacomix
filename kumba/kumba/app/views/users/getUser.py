from django.contrib.auth.models import User

def get_user_username(username):
    """
    Retourne un utilisateur en fonction de son nom d'utilisateur.

    Args:
        username (str): Le nom d'utilisateur de l'utilisateur à retourner.

    Returns:
        User: L'utilisateur correspondant au nom d'utilisateur spécifié.
    """
    return User.objects.get(username=username)

def get_user_email(email):
    return User.objects.get(email=email)
