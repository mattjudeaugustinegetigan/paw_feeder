from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import Pet
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'feedapp/home.html')

def login_view(request):
    return render(request, 'feedapp/login.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'feedapp/signup.html', {'form': form})

def profile(request):
    pets = Pet.objects.filter(user=request.user)
    return render(request, 'feedapp/profile.html', {'pets': pets})

def add_pet(request):
    if request.method == 'POST':
        pet_name = request.POST.get('name')
        pet_age = request.POST.get('age')
        pet_breed = request.POST.get('breed')
        new_pet = Pet(name=pet_name, age=pet_age, breed=pet_breed, user=request.user)
        new_pet.save()
        return redirect('profile')
    return render(request, 'feedapp/add_pet.html')

def add_dogorcat(request):
    return render(request, 'feedapp/add_dogorcat.html')
