from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages 


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password1']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalide credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request, "User name already exist.")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already exist.")
                return redirect('register')
            else :
                user = User. objects.create(username=user_name, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                return redirect('login')

        else:
            messages.info(request, "Password not match.")
            return redirect('register')
        
        return redirect('/')
    return render(request, "register.html")