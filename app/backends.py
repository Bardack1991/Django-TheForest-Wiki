from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse

def inicio_sesion(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('cuenta')
        else:
            return render(request, 'app/inicio_sesion_wiki.html', {'error': 'Email o contraseña incorrectos'})
    else:
        return render(request, 'app/inicio_sesion_wiki.html')