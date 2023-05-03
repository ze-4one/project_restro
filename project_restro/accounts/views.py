from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
class RegistrationView(View):
    def get(self, request):
        return render(request, 'authentication/register.html')
    
    def post(self, request):
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(first_name=first_name, last_name=last_name,
                                        email=email, username=username)
        user.set_password(password)
        user.is_staff = False
        user.is_active = True
        user.save()
        messages.success(request, "Registered Successfully..")
        return redirect("register")

class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login Succesful')
            return redirect("menu-list")
        else:
            messages.error(request, "Login Failed")
            return redirect("login")
        
class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.info(request, "You are logged out..")
        return redirect("login")