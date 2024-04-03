from django.shortcuts import render


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
    return render(request, 'app/inicio_sesion_wiki.html')

def logros(request):
    return render(request, 'app/logros.html')

def lugares(request):
    return render(request, 'app/lugarestf.html')

def menuPrincipal(request):
    return render(request, 'app/menuprincipal_wiki.html')

def miCuenta(request):
    return render(request, 'app/micuentatf.html')

def recuperarContraseña(request):
    return render(request, 'app/recuperarcontra.html')

def registro(request):
    return render(request, 'app/registrase_wiki.html')