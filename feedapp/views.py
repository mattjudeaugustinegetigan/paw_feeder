from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import Pet
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  # Import messages for feedback
from django.contrib.auth.forms import AuthenticationForm  # For login form

def home(request):
    return render(request, 'feedapp/home.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)  # Use AuthenticationForm for login
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to homepage after successful login
            else:
                messages.error(request, "No user found with this username or invalid password.")  # Error message
        else:
            messages.error(request, "Invalid username or password.")  # Error message
    else:
        form = AuthenticationForm()
    
    return render(request, 'feedapp/login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Sign up successful! You can now log in.")  # Success message
            return redirect('login')
        else:
            messages.error(request, "Sign up failed. Please correct the errors below.")  # Error message
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
        messages.success(request, "Pet added successfully!")  # Success message
        return redirect('profile')
    
    return render(request, 'feedapp/add_pet.html')

def add_dogorcat(request):
    return render(request, 'feedapp/add_dogorcat.html')
