import numpy as np
from metodos.InputFixed import InputFixed

class PuntoFijo:
    def PuntoFijo(f,g,x0,tol,niter):
        f = InputFixed.CorregirFuncion(f)
        g = InputFixed.CorregirFuncion(g)
        solucion = 0
        resultados = []
        x = x0
        c = 0
        Error = 100
        fx = eval(f)

        resultados.append([c,"{:.5f}".format(x),"{:.3e}".format(fx),Error])

        while Error > tol and fx != 0 and c < niter:
            xAnterior = x
            x = eval(g)
            fx = eval(f)
            c = c + 1
            Error = abs(x - xAnterior)
            resultados.append([c,"{:.5f}".format(x),"{:.3e}".format(fx),"{:.2e}".format(Error)])

        if fx == 0:
            solucion = "{:.5f}".format(x)
            mensaje = str(solucion) + " es raiz de f(x)"
            return resultados, mensaje, solucion
        elif Error < tol:
            solucion = "{:.5f}".format(x)
            mensaje = str(solucion) + " es una aproximacion de un raiz de f(x) con una tolerancia " + str(tol)
            return resultados, mensaje, solucion
        else:
            solucion = "{:.5f}".format(x)
            mensaje = "Fracaso en " + str(niter) + " iteraciones"
            return resultados, mensaje, None
    
    
    def PuntoFijoRel(f,g,x0,tol,niter):
        f = InputFixed.CorregirFuncion(f)
        g = InputFixed.CorregirFuncion(g)
        solucion = 0
        resultados = []
        x = x0
        c = 0
        Error = 100
        fx = eval(f)

        resultados.append([c,"{:.5f}".format(x),"{:.3e}".format(fx),Error])

        while Error > tol and fx != 0 and c < niter:
            xAnterior = x
            x = eval(g)
            fx = eval(f)
            c = c + 1
            Error = abs((x - xAnterior)/x)
            resultados.append([c,"{:.5f}".format(x),"{:.3e}".format(fx),"{:.2e}".format(Error)])

        if fx == 0:
            solucion = "{:.5f}".format(x)
            mensaje = str(solucion) + " es raiz de f(x)"
            return resultados, mensaje, solucion
        elif Error < tol:
            solucion = "{:.5f}".format(x)
            mensaje = str(solucion) + " es una aproximacion de un raiz de f(x) con una tolerancia " + str(tol)
            return resultados, mensaje, solucion
        else:
            solucion = "{:.5f}".format(x)
            mensaje = "Fracaso en " + str(niter) + " iteraciones"
            return resultado, mensaje, None
