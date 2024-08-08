from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
import random
import json
from django.http import JsonResponse

User = get_user_model()

def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        role = request.POST.get('role')
        photo = request.FILES.get('photo')
        otp = request.POST.get('otp')

        if password != confirm_password:
            return render(request, 'register.html', {'error': 'Passwords do not match'})

        if otp != request.session.get('otp'):
            return render(request, 'register.html', {'error': 'Invalid OTP'})

        user = User.objects.create_user(
            username=email,
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            role=role,
            profile_image=photo
        )

        send_mail(
            'Registration Successful',
            'Welcome to our platform! Your registration was successful.',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

        return redirect('login')
    return render(request, 'register.html')

def send_otp(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        otp = random.randint(100000, 999999)
        request.session['otp'] = str(otp)

        send_mail(
            'Your OTP Code',
            f'Hello User, Your OTP code is {otp}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )
        return JsonResponse({'message': 'OTP sent'})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def forgot_password(request):
    return render(request, 'forgot_password.html')