from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def update_user(request):
    if request.method == 'POST':
        # Obtenez l'utilisateur actuel
        user = request.user
        # Mettez à jour les informations de l'utilisateur
        user.username=request.POST['username']
        user.nom=request.POST['nom']
        user.prenom=request.POST['prenom']
        user.tel=request.POST['tel']
        user.pays=request.POST['pays']
        user.email=request.POST['email']
        user.email = request.POST['email']
        user.save()
        return redirect('home')
    else:
        return render(request, 'update_user.html')