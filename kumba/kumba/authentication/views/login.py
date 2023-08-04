from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def login(request):
    if request.method == 'POST':
        # Vérifiez si les données de connexion sont valides
        user = auth.authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is not None:
            # Connectez l'utilisateur
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Les informations de connexion ne correspondent pas.'})
    else:
        return render(request, 'login.html')

