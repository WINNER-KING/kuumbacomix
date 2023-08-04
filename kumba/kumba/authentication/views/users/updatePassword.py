from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def update_password(request):
    if request.method == 'POST':
        # Vérifiez si les données de formulaire sont valides
        if request.POST['password1'] == request.POST['password2']:
            # Obtenez l'utilisateur actuel
            user = request.user
            if request.POST['password'] == user.get_password:
                # Mettez à jour le mot de passe de l'utilisateur
                user.set_password(request.POST['password1'])
                user.save()
                # Connectez l'utilisateur au nouveau mot de passe
                auth.login(request, user)
                return redirect('home')
            else:
                return render(request, 'update_password.html', {'error': "L'ancien mots de passe est incorrect."})
        else:
            return render(request, 'update_password.html', {'error': 'Les nouveaux mots de passe ne correspondent pas.'})
    else:
        return render(request, 'update_password.html')