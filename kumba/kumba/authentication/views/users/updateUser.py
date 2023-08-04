from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def update_user(request):
    if request.method == 'POST':
        # Obtenez l'utilisateur actuel
        user = request.user
        # Mettez à jour les informations de l'utilisateur
        username=request.POST['username']
        nom=request.POST['nom']
        prenom=request.POST['prenom']
        tel=request.POST['tel']
        pays=request.POST['pays']
        email=request.POST['email']
        user.email = request.POST['email']
        user.save()
        return redirect('home')
    else:
        return render(request, 'update_user.html')