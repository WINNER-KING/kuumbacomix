from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def delete_user(request):
    if request.method == 'POST':
        # Vérifiez si les données de formulaire sont valides
        if request.POST['role'] :
            # Obtenez l'utilisateur actuel
            user = request.user

            # Supprimer un utilisateur
            user.delete()
           
            return redirect('home')
        else:
            return render(request, 'update_role.html', {'error': "Le role n'a pas  été spécifié."})
    else:
        return render(request, 'update_role.html')