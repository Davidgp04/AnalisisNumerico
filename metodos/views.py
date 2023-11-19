from django.shortcuts import render
from urllib.parse import quote, unquote
from metodos.Biseccion import Biseccion
from metodos.Grafica import Grafica
from metodos.InputFixed import InputFixed
from metodos.Newton import NewtonRaphson
from metodos.Secante import Secante
from metodos.PuntoFijo import PuntoFijo
from metodos.ReglaFalsa import ReglaFalsa
from metodos.RaicesMultiples import RaicesMultiples
import matlab.engine
import numpy as np

eng = matlab.engine.start_matlab()

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
    solucion = None
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
            resultado, mensaje, solucion = ReglaFalsa.ReglaFalsa(funcion, a, b, tol, niter)
            funcion = quote(funcion)
            print(funcion)
        else:
            resultado, mensaje = ReglaFalsa.ReglaFalsaRel(funcion, a, b, tol, niter)
    return render(request, 'reglafalsa.html', {'resultado': resultado, 'mensaje': mensaje, 'solucion': solucion, 'funcion': funcion})

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

def GraficaSolucion(request, funcion, solucion):
    Grafica = None
    if funcion and solucion:
        funcion = unquote(funcion)
        Grafica = Grafica.GraficarSolucion(funcion, solucion)

    return render(request, 'graficaSolucion.html', {'Grafica': Grafica, 'funcion': funcion})

def codificar_funcion(funcion):
    # Divide la función en segmentos
    segmentos = funcion.split(' ')

    # Codifica cada segmento y guárdalo en una lista
    segmentos_codificados = [quote(segmento) for segmento in segmentos]

    # Une los segmentos codificados con espacios en blanco
    funcion_codificada = ' '.join(segmentos_codificados)

    return funcion_codificada

def jacobiSeid(request):
    datos_iteraciones = None
    mensaje = ""
    converge = ""

    if request.method == 'POST':
        filas = request.POST['rows']
        columnas = request.POST['columns']
        filas = int(filas)
        columnas = int(columnas)
        matrizA = [[0 for _ in range(columnas)] for _ in range(filas)]
        vectorB = [[0 for _ in range(1)]for _ in range(filas)]
        vectorX0 = [[0 for _ in range(1)]for _ in range(filas)]
        indice = 1
        for i in range(0, filas):
            for j in range(0, columnas):
                elemento = f'element_{indice}'
                matrizA[i][j] = int(request.POST[elemento])
                indice += 1
        indice = 1
        for i in range(0, filas):
            answer = f'answer_{indice}'
            vectorB[i][0] = int(request.POST[answer])
            indice += 1
        indice = 1
        for i in range(0, filas):
            initial = f'initial_{indice}'
            vectorX0[i][0] = int(request.POST[initial])
            indice += 1
        A = matlab.double(matrizA)
        b = matlab.double(vectorB)
        x0 = matlab.double(vectorX0)
        tol = request.POST['Tol']
        tol = float(tol)
        iteraciones = request.POST['Iter']
        iteraciones = int(iteraciones)
        met = request.POST['met']
        met = int(met)
        resultados = eng.MatJacobiSeid(x0,A,b,tol,iteraciones,met,nargout = 5)
        E = resultados[0]
        S = resultados[1]
        Iteraciones = resultados[2]
        x_values = np.array(Iteraciones)
        x_values = x_values.T
        valoresX = x_values.tolist()
        radioEspectral = resultados[4]
        solucion = resultados[3]

        for i in range(len(valoresX)):
            for j in range(len(valoresX[i])):
                valoresX[i][j] = "{:.5f}".format(valoresX[i][j])
                
        Error = np.array(E)
        for i in range(len(Error[0])):
            Error[0][i] = "{:.3e}".format(Error[0][i])
            
        datos_iteraciones = list(zip(valoresX, Error[0]))
        mensaje = str(S) + ' ' +  str(solucion)
        converge = solucion[0]
        if converge == 'E':
            converge = 'El metodo converge con un ρ(T) de ' + str(radioEspectral)
        else:
            converge = 'El metodo no converge porque su ρ(T) es de ' + str(radioEspectral)
        
        
    return render(request, 'jacobiSeid.html', {'datos_iteraciones': datos_iteraciones, 'mensaje':mensaje, 'converge':converge})


def SOR(request):
    datos_iteraciones = None
    mensaje = ''
    converge = ''
    if request.method == 'POST':
        filas = request.POST['rows']
        columnas = request.POST['columns']
        filas = int(filas)
        columnas = int(columnas)
        matrizA = [[0 for _ in range(columnas)] for _ in range(filas)]
        vectorB = [[0 for _ in range(1)]for _ in range(filas)]
        vectorX0 = [[0 for _ in range(1)]for _ in range(filas)]
        indice = 1
        for i in range(0, filas):
            for j in range(0, columnas):
                elemento = f'element_{indice}'
                matrizA[i][j] = int(request.POST[elemento])
                indice += 1
        indice = 1
        for i in range(0, filas):
            answer = f'answer_{indice}'
            vectorB[i][0] = int(request.POST[answer])
            indice += 1
        indice = 1
        for i in range(0, filas):
            initial = f'initial_{indice}'
            vectorX0[i][0] = int(request.POST[initial])
            indice += 1
        A = matlab.double(matrizA)
        b = matlab.double(vectorB)
        x0 = matlab.double(vectorX0)
        tol = request.POST['Tol']
        tol = float(tol)
        iteraciones = request.POST['Iter']
        iteraciones = int(iteraciones)
        valorW = request.POST['w']
        valorW = float(valorW)
        resultados = eng.SOR(x0, A, b, tol, iteraciones, valorW,nargout = 5)
        E = resultados[0]
        S = resultados[1]
        Iteraciones = resultados[2]
        x_values = np.array(Iteraciones)
        x_values = x_values.T
        valoresX = x_values.tolist()
        radioEspectral = resultados[4]
        solucion = resultados [3]

        for i in range(len(valoresX)):
            for j in range(len(valoresX[i])):
                valoresX[i][j] = "{:.5f}".format(valoresX[i][j])

        Error = np.array(E)
        for i in range(len(Error[0])):
            Error[0][i] = "{:.3e}".format(Error[0][i])

        datos_iteraciones = list(zip(valoresX, Error[0]))
        mensaje = str(S) + ' ' +  str(solucion)
        converge = solucion[0]
        if converge == 'E':
            converge = 'El metodo converge con un ρ(T) de ' + str(radioEspectral)
        else:
            converge = 'El metodo no converge porque su ρ(T) es de ' + str(radioEspectral)
    return render(request, 'SOR.html', {'datos_iteraciones': datos_iteraciones, 'mensaje':mensaje, 'converge':converge})