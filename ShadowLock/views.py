from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .models import *
from .forms import *

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')  # Redirect logged-in users to home or dashboard
        return view_func(request, *args, **kwargs)
    return wrapper_func

@unauthenticated_user
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")

    return render(request, 'pages/login.html')

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully!")
    return redirect('home')

# Create your views here.
def Home(request: object) -> render:
    return render(request,'pages/index.html')

@login_required(login_url='login')
def Dashboard(request: object) -> render:
    return render(request, 'pages/dashboard.html')

@login_required(login_url='login')
def passwords(request: object) -> render:
    if request.headers.get("HX-Request"):
        if request.method == "GET":
            passwords_instance = Passwords.objects.filter(created_by=request.user).order_by('-created_at')
            context = {
                "instances" : passwords_instance,
            }
            return render(request, "components/cards.html", context=context)
    return redirect('dashboard')

@login_required
def password_create_view(request):
    if request.headers.get("HX-Request"):
        if request.method == "POST":
            form = PasswordsForm(request.POST, user=request.user)
            print("Post inittited")
            if form.is_valid():
                print("Form is valid")
                password_instance = form.save(user=request.user)
                password_entry = Passwords.objects.get(id=password_instance.id, created_by=request.user)  # Explicitly fetch
                return render(request, "components/cards.html", {"instances": [password_entry]})  # Render only this entry

        else:
            form = PasswordsForm(user=request.user)
    return render(request, 'components/password_form.html', {'form': form})

@login_required(login_url='login')
def environments(request: object) -> render:
    if request.headers.get("HX-Request"):
        if request.method == "GET":
            environments_instance = Environment.objects.filter(created_by=request.user).order_by('-created_at')
            context = {
                "instances" : environments_instance,
            }
            return render(request, "components/cards.html", context=context)
    return redirect('dashboard')

@login_required(login_url='login')
def shared(request: object, id: int = None) -> render:
    if request.headers.get("HX-Request"):
        if request.method == "GET":
            passwords_instance = Passwords.objects.filter(shared_with=request.user).order_by('-created_at')
            environments_instance = Environment.objects.filter(shared_with=request.user).order_by('-created_at')
            context = {
                "instances" : list(passwords_instance) + list(environments_instance),
            }
            return render(request, "components/cards.html", context=context)
    return redirect('dashboard')
