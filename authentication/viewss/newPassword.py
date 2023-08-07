from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def new_password(request):
    if request.method == 'POST':
        # Vérifiez si les données de formulaire sont valides
        if request.POST['password1'] == request.POST['password2']:
            # Obtenez l'utilisateur actuel
            user = request.user
            # Mettez à jour le mot de passe de l'utilisateur
            user.set_password(request.POST['password1'])
            user.save()
            # Connectez l'utilisateur au nouveau mot de passe
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'new_password.html', {'error': 'Les mots de passe ne correspondent pas.'})
    else:
        return render(request, 'new_password.html')