from django.shortcuts import render
from metodos.Biseccion import Biseccion
def index(request):
    return render(request, 'home.html', {})

def metodos(request):
    return render(request, 'metodos.html', {})

def biseccion(request):
    resultado = []
    if request.method == 'POST':
        funcion = request.POST['Funcion']
        a = request.POST['LimiteInferior']
        b = request.POST['LimiteSuperior']
        tol = request.POST['Tol']
        niter = request.POST['Iteraciones']
        
        a = float(a)
        b = float(b)
        tol = float(tol)
        niter = int(niter)
        
        resultado = Biseccion.biseccion(funcion, a, b, tol, niter)
    return render(request, 'biseccion.html', {'resultado': resultado})