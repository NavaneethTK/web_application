from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password, check_password

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def success(request):
    return render(request, 'success.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['Email']
        password = request.POST['password']

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'Invalid email or password')
            return redirect('login')

        if check_password(password, user.password):
            messages.success(request, 'You are login successfully')
            return redirect('success')
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('login')

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        firstname = request.POST['Firstname']
        lastname = request.POST['Lastname']
        phone_number = request.POST['PhoneNumber']
        email = request.POST['Email']
        gender = request.POST['Gender']
        password = request.POST['password']  # Password should be hashed

        hashed_password = make_password(password)
        # Create the CustomUser instance
        user = User(
            firstname=firstname,
            lastname=lastname,
            phone_number=phone_number,
            email=email,
            gender=gender,
            password=hashed_password
        )
        user.save()

        # Optionally, you can pass some data to the output template
        context = {
            'Firstname': firstname,
            'Lastname': lastname,
            'PhoneNumber': phone_number,
            'Email': email,
            'Gender': gender,
        }
        return render(request, 'output.html', context)
    else:
        return render(request, 'index.html')


