from django.shortcuts import render
from metodos.Biseccion import Biseccion
from metodos.Grafica import Grafica
from metodos.InputFixed import InputFixed
from metodos.Newton import NewtonRaphson
from metodos.Secante import Secante
from metodos.PuntoFijo import PuntoFijo
from metodos.ReglaFalsa import ReglaFalsa
from metodos.RaicesMultiples import RaicesMultiples

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

def reglafalsa(request):
    resultado = []
    mensaje = ""
    if request.method == 'POST':
        funcion = request.POST['Funcion']
        a = request.POST['LimiteInferior']
        b = request.POST['LimiteSuperior']
        tol = request.POST['Tol']
        niter = request.POST['Iteraciones']
        error = request.POST['Error']
        
        error = int(error)
        a = float(a)
        b = float(b)
        tol = float(tol)
        niter = int(niter)

        if(error == 1):
            resultado, mensaje = ReglaFalsa.ReglaFalsa(funcion, a, b, tol, niter)
        else:
            resultado, mensaje = ReglaFalsa.ReglaFalsaRel(funcion, a, b, tol, niter)
    return render(request, 'reglafalsa.html', {'resultado': resultado, 'mensaje': mensaje})

def newtonRaphson(request):
    resultado = []
    mensaje = ""
    if request.method == 'POST':
        funcion = request.POST['Funcion']
        funcionDerivada = request.POST['primeraDerivada']
        x0 = request.POST['valorInicial']
        tol = request.POST['Tol']
        niter = request.POST['Iteraciones']
        error = request.POST['Error']
        
        error = int(error)
        x0 = float(x0)
        tol = float(tol)
        niter = int(niter)
        if(error == 1):
            resultado, mensaje = NewtonRaphson.Newton(funcion,funcionDerivada, x0, tol, niter)
        else:
            resultado, mensaje = NewtonRaphson.NewtonRel(funcion,funcionDerivada, x0, tol, niter)
    return render(request, 'newtonRaphson.html',{'resultado': resultado, 'mensaje': mensaje})

def secante(request):
    resultado = []
    mensaje = ""
    if request.method == 'POST':
        f = request.POST['Funcion']
        a = request.POST['inicialx0']
        b = request.POST['inicialx1']
        tol = request.POST['Tol']
        niter = request.POST['Iteraciones']
        error = request.POST['Error']
        
        error = int(error)
        a = float(a)
        b = float(b)
        tol = float(tol)
        niter = int(niter)
        Fcorregida = InputFixed.CorregirFuncion(f)
        if(error == 1):
            resultado, mensaje = Secante.Secante(Fcorregida,a,b,tol,niter)
        else:
            resultado, mensaje = Secante.SecanteRel(Fcorregida,a,b,tol,niter)
       
    return render(request, 'secante.html',{'resultado': resultado, 'mensaje': mensaje})

def raicesMultiples(request):
    resultado = []
    mensaje = ""
    if request.method == 'POST':
        Funcion = request.POST['Funcion']
        PrimeraDerivada = request.POST['PrimeraDerivada']
        SegundaDerivada = request.POST['SegundaDerivada']
        x0 = request.POST['ValorInicial']
        tol = request.POST['Tol']
        niter = request.POST['Iteraciones']
        error = request.POST['Error']
        
        error = int(error)
        x0 = float(x0)
        tol = float(tol)
        niter = int(niter)
        if(error == 1):
           
            resultado, mensaje = RaicesMultiples.RaicesMultiples(Funcion ,PrimeraDerivada ,SegundaDerivada , x0, tol, niter)
        else:
           
            resultado, mensaje = RaicesMultiples.RaicesMultiplesRel(Funcion ,PrimeraDerivada ,SegundaDerivada , x0, tol, niter)
    return render(request, 'raicesmultiples.html',{'resultado': resultado, 'mensaje': mensaje})

def puntofijo(request):
    resultado = []
    mensaje = ""
    if request.method == 'POST':
        Funcionf = request.POST['Funcionf']
        Funciong = request.POST['Funciong']
        x0 = request.POST['ValorInicial']
        tol = request.POST['Tol']
        niter = request.POST['Iteraciones']
        error = request.POST['Error']
        
        error = int(error)
        x0 = float(x0)
        tol = float(tol)
        niter = int(niter)
        if(error == 1):
            resultado, mensaje = PuntoFijo.PuntoFijo(Funcionf,Funciong, x0, tol, niter)
        else:
             resultado, mensaje = PuntoFijo.PuntoFijoRel(Funcionf,Funciong, x0, tol, niter)
    return render(request, 'puntofijo.html',{'resultado': resultado, 'mensaje': mensaje})

def biseccion(request):
    resultado = []
    mensaje = ""
    if request.method == 'POST':
        funcion = request.POST['Funcion']
        limiteInf = request.POST['LimiteInferior']
        limiteSup = request.POST['LimiteSuperior']
        tol = request.POST['Tol']
        niter = request.POST['Iteraciones']
        error = request.POST['Error']
        
        error = int(error)
        limiteInf = float(limiteInf)
        limiteSup = float(limiteSup)
        tol = float(tol)
        niter = int(niter)
        Fcorregida = InputFixed.CorregirFuncion(funcion)
        if(error == 1):
            resultado, mensaje = Biseccion.biseccion(Fcorregida, limiteInf, limiteSup, tol, niter)
        else:
            resultado, mensaje = Biseccion.biseccionRel(Fcorregida, limiteInf, limiteSup, tol, niter)
    return render(request, 'biseccion.html', {'resultado': resultado, 'mensaje': mensaje})