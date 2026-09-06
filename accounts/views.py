from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as django_login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth


# LOGIN


def login(request):

    if request.method == "POST":

        email = request.POST.get("identifier")
        password = request.POST.get("password")
        remember_me = request.POST.get("remember_me")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "Email is not registered yet")
            return redirect("login")

        user = auth.authenticate(
            username=user.username,
            password=password
        )

        if user is not None:

            auth.login(request, user)

            if remember_me:
                request.session.set_expiry(360000)
            else:
                request.session.set_expiry(0)

            return redirect("home")

        else:

            messages.error(request, "Invalid Password")
            return redirect("login")

    return render(request, "login.html")

# LOGOUT

def logout(request):
    auth.logout(request)

    return redirect('home')




# SIGNUP

def signup(request):

    if request.method == 'POST':

        full_name = request.POST.get('username')
        email = request.POST.get('identifier')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Check passwords
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')

        # Check email
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered')
            return redirect('signup')

        # Create username from email
        username = email.split('@')[0]

        # If username already exists
        if User.objects.filter(username=username).exists():
            username = email

        # Create account
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=full_name
        )

        messages.success(
            request,
            'CONGRATULATIONS!!! You have created your account in LUNOIR 🥳'
        )

        return redirect('signup')

    return render(request, 'signup.html')

