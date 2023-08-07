from django.contrib.auth.models import User

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
