from django.shortcuts import render

def index(request):
    return render(request, 'home.html', {})

def metodos(request):
    return render(request, 'metodos.html', {})