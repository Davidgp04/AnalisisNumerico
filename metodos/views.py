from django.shortcuts import render
from metodos.Biseccion import Biseccion
from metodos.Grafica import Grafica
from metodos.InputFixed import InputFixed
def index(request):
    grafica = None
    if request.method == 'POST':
        grafica = None
        funcion = request.POST['Funcion']
        Fcorregida = InputFixed.CorregirFuncion(funcion) 
        grafica = Grafica.Graficar(Fcorregida)
    return render(request, 'home.html', {'grafica': grafica})

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