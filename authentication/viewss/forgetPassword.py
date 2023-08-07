from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def forgot_password(request):
    if request.method == 'POST':
        # Vérifiez si l'adresse e-mail est valide
        try:
            user = User.objects.get(email=request.POST['email'])
        except User.DoesNotExist:
            return render(request, 'forgot_password.html', {'error': "L'adresse e-mail n\'est pas enregistrée."})
        else:
            # Envoyez un e-mail à l'utilisateur avec un lien pour réinitialiser son mot de passe
            user.send_password_reset_email()
            return render(request, 'forgot_password.html', {'success': 'Un e-mail a été envoyé à votre adresse e-mail avec un lien pour réinitialiser votre mot de passe.'})
    else:
        return render(request, 'forgot_password.html')