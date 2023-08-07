from django.shortcuts import render, redirect
from django.contrib.auth.models import User
#from django.contrib.authenticate.views import .*

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

def logout(request):
    auth.logout(request)
    return redirect('home')

def add_role(request):
    if request.method == 'POST':
        # Vérifiez si les données de formulaire sont valides
        if request.POST['role'] :
            # Obtenez l'utilisateur actuel
            user = request.user
            # Attribuer un rôle à un utilisateur
            user.add_role(request.POST['role'])
           
            return redirect('home')
        else:
            return render(request, 'update_role.html', {'error': "Le role n'a pas  été spécifié."})
    else:
        return render(request, 'update_role.html')
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

def get_all_users():
    return User.objects.all()

def get_user_username(username):

    return User.objects.get(username=username)

def get_user_email(email):
    return User.objects.get(email=email)

def get_user_data(data):
    if request.method == 'POST':
        # Vérifiez si les données de formulaire sont valides
        data = request.POST
        for key,datum in data:
            if hasattr(user, key): data.remove(key)
        if data == []: 
            return User.objects.all()
        return User.objects.filter(data)
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
           
            return redirect('home')
        else:
            return render(request, 'update_role.html', {'error': "Le role n'a pas  été spécifié."})
    else:
        return render(request, 'update_role.html')

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