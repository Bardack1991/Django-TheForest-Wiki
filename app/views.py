from django.shortcuts import render

def home(request):
    return render(request, 'app/menuprincipal_wiki.html')