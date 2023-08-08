from django.shortcuts import render, redirect
from django.contrib.auth.models import User
import json
from django.http import JsonResponse


def forgot_password(request):
    if request.method == 'POST':
        # Vérifiez si l'adresse e-mail est valide
        try:
            user = User.objects.get(email=request.POST['email'])
        except User.DoesNotExist:
            #return render(request, 'forgot_password.html', {'error': "L'adresse e-mail n\'est pas enregistrée."})
            return JsonResponse({'error': 'User not found'}, status=404)
        else:
            # Envoyez un e-mail à l'utilisateur avec un lien pour réinitialiser son mot de passe
            user.send_password_reset_email()
            #return render(request, 'forgot_password.html', {'success': 'Un e-mail a été envoyé à votre adresse e-mail avec un lien pour réinitialiser votre mot de passe.'})
            return JsonResponse({'success': 'Un e-mail a été envoyé à votre adresse e-mail avec un lien pour réinitialiser votre mot de passe.'}, status=200)
    else:
        #return render(request, 'forgot_password.html')
        return JsonResponse({'error': "la méthode utilisé n'est pas convenable. La méthode POST est requise"}, status=404)


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
            #return redirect('home')
            return JsonResponse({'succes': "Authentification réussi"}, status=200)

        else:
            #return render(request, 'login.html', {'error': 'Les informations de connexion ne correspondent pas.'})
            return JsonResponse({'error': 'Les informations de connexion ne correspondent pas.'}, status=500)

    else:
        return JsonResponse({'error': "la méthode utilisé n'est pas convenable. La méthode POST est requise"}, status=404)

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
            #return redirect('home')
            return JsonResponse({'succes': "Changement de mot de passe réussi"}, status=200)
        else:
            #return render(request, 'new_password.html', {'error': 'Les mots de passe ne correspondent pas.'})
            return JsonResponse({'error': 'Les mots de passe ne correspondent pas.'}, status=500)
    else:
        #return render(request, 'new_password.html')
        return JsonResponse({'error': "la méthode utilisé n'est pas convenable. La méthode POST est requise"}, status=404)

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
            #return redirect('home')
            return JsonResponse({'succes': "Inscription réussi"}, status=200)
        else : 
            return JsonResponse({'error': "Les mots de passes ne sont pas identiques"}, status=500)
    else:
        return JsonResponse({'error': "la méthode utilisé n'est pas convenable. La méthode POST est requise"}, status=404)

def logout(request):
    auth.logout(request)
    #return redirect('home')
    return JsonResponse({'succes': "Déconnection réussi"}, status=200)

def add_role(request):
    if request.method == 'POST':
        # Vérifiez si les données de formulaire sont valides
        if request.POST['role'] :
            # Obtenez l'utilisateur actuel
            user = request.user
            # Attribuer un rôle à un utilisateur
            user.add_role(request.POST['role'])
           
            #return redirect('home')
            return JsonResponse({'succes': "Ajout de role réussi"}, status=200)
        else:
            #return render(request, 'update_role.html', {'error': "Le role n'a pas  été spécifié."})
            return JsonResponse({'error': "Le role n'a pas  été spécifié."}, status=500)
    else:
        #return render(request, 'update_role.html')
        return JsonResponse({'error': "la méthode utilisé n'est pas convenable. La méthode POST est requise"}, status=404)

def delete_user(request):
    if request.method == 'POST':
        user = request.user
        # Supprimer un utilisateur
        user.delete()
        
        #return redirect('home')
        return JsonResponse({'succes': "Suppression de user réussi"}, status=200)
    else:
        #return render(request, 'update_role.html')
        return JsonResponse({'error': "la méthode utilisé n'est pas convenable. La méthode POST est requise"}, status=404)

def get_all_users():
    return JsonResponse(User.objects.all(), content_type='application/json')


def get_user_username(username):
    try:
        data = User.objects.get(username=username)
        return JsonResponse(data, content_type='application/json')
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

def get_user_email(email):
    try:
        data =  User.objects.get(email=email)
        return JsonResponse(data, content_type='application/json')
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

def get_user_data(data):
    if request.method == 'POST':
        # Vérifiez si les données de formulaire sont valides
        data = request.POST
        for key,datum in data:
            if hasattr(user, key): data.remove(key)
        if data == []: 
            ret =  User.objects.all()
        else : ret =  User.objects.filter(data)
        return JsonResponse(ret, content_type='application/json')
    else:
        return render(request, 'filter_users.html')
def remove_role(request):
    if request.method == 'POST':
        # Vérifiez si les données de formulaire sont valides
        if request.POST['role'] :
            # Obtenez l'utilisateur actuel
            user = request.user

            # Supprimer un rôle d'un utilisateur
            user.remove_role(request.POST['role'])
           
            #return redirect('home')
            return JsonResponse({'succes': "Suppression de role réussi"}, status=200)
        else:
            #return render(request, 'update_role.html', {'error': "Le role n'a pas  été spécifié."})
            return JsonResponse({'error': "Le role n'a pas  été spécifié."}, status=500)
    else:
        #return render(request, 'update_role.html')
        return JsonResponse({'error': "la méthode utilisé n'est pas convenable. La méthode POST est requise"}, status=404)

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
                #return redirect('home')
                return JsonResponse({'succes': "Mise a jour de mot de passe réussi",'user': user}, status=200)
            else:
                #return render(request, 'update_password.html', {'error': "L'ancien mots de passe est incorrect."})
                return JsonResponse({'error': "L'ancien mots de passe est incorrect."}, status=500)
        else:
            #return render(request, 'update_password.html', {'error': 'Les nouveaux mots de passe ne correspondent pas.'})
            return JsonResponse({'error': "Les nouveaux mots de passe ne correspondent pas."}, status=500)
    else:
        #return render(request, 'update_password.html')
        return JsonResponse({'error': "la méthode utilisé n'est pas convenable. La méthode POST est requise"}, status=404)

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
        #return redirect('home')
        return JsonResponse({'succes': "Mise a jour de user réussi",'user': user}, status=200)
    else:
        #return render(request, 'update_user.html')
        return JsonResponse({'error': "la méthode utilisé n'est pas convenable. La méthode POST est requise"}, status=404)