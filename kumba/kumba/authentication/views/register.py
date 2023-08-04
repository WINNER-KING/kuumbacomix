from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        # Vérifiez si les données de formulaire sont valides
        if request.POST['password1'] == request.POST['password2']:
            # Créez un nouvel utilisateur
            user = User.objects.create(
                username=request.POST['username'],
                nom=request.POST['nom'],
                prenom=request.POST['prenom'],
                tel=request.POST['tel'],
                pays=request.POST['pays'],
                email=request.POST['email'],
                password=request.POST['password']
            )
            # Connectez l'utilisateur
            auth.login(request, user)
            return redirect('home')
    else:
        return render(request, 'register.html')