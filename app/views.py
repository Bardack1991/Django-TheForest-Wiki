from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import RegistroUsuarioForm
from .forms import EditarUsuarioForm
from django.http import HttpRequest

@login_required
def miCuenta(request: HttpRequest):
    if request.method == 'POST':
        form = EditarUsuarioForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('cuenta')
    else:
        form = EditarUsuarioForm(instance=request.user)
    return render(request, 'app/micuentatf.html', {'form': form})

def registro(request: HttpRequest):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicioSesion')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'app/registrase_wiki.html', {'form': form})

def animales(request):
    return render(request, 'app/Animales.html')

def armas(request):
    return render(request, 'app/Armas.html')

def construcciones(request):
    return render(request, 'app/Construcciones.html')

def consumibles(request):
    return render(request, 'app/Consumibles.html')

def enemigos(request):
    return render(request, 'app/Enemigos.html')

def flora(request):
    return render(request, 'app/Flora.html')

def forowiki(request):
    return render(request, 'app/forowiki.html')

def historia(request):
    return render(request, 'app/historia.html')

def inicioSesion(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('cuenta')
        else:
            return render(request, 'app/inicio_sesion_wiki.html', {'error': 'Email o contraseña incorrectos'})
    else:
        return render(request, 'app/inicio_sesion_wiki.html')

def logros(request):
    return render(request, 'app/logros.html')

def lugares(request):
    return render(request, 'app/lugarestf.html')

def menuPrincipal(request):
    return render(request, 'app/menuprincipal_wiki.html')

def recuperarContraseña(request):
    return render(request, 'app/recuperarcontra.html')
