from django.shortcuts import redirect
from django.shortcuts import render, redirect

def logout(request):
    auth.logout(request)
    return redirect('home')