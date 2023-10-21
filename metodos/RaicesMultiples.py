from math import *
import numpy as np
from tabulate import tabulate
from metodos.InputFixed import InputFixed

class RaicesMultiples:
    def RaicesMultiples(f, df1, df2, x0, tol, niter):
        f = InputFixed.CorregirFuncion(f)
        df1 = InputFixed.CorregirFuncion(df1)
        df2 = InputFixed.CorregirFuncion(df2)
        solucion = 0
        x = x0
        fx = eval(f)
        df1x = eval(df1)
        df2x = eval(df2)
        Error = 100
        c = 0
        resultados = []
        resultados.append([c,x,fx,100])
        while Error > tol and c < niter and fx != 0:
            x = x0 - (fx * df1x) / ((df1x**2) - (fx*df2x))
            fx = eval(f)
            df1x = eval(df1)
            df2x = eval(df2)

            c = c + 1
            Error = abs(x - x0)
            resultados.append([c,"{:.3e}".format(x),"{:.3e}".format(fx),"{:.3e}".format(Error)])

            x0 = x

        if fx == 0:
            solucion = "{:.5e}".format(x)
            mensaje = str(solucion) + " es raiz de f(x)"
            return resultados, mensaje
        elif Error <= tol:
            solucion = "{:.5e}".format(x)
            mensaje = str(solucion) + " es una aproximacion de un raiz de f(x) con una tolerancia " + str(tol)
            print(f)
            print(df1)
            return resultados, mensaje
        else:
            solucion = "{:.5f}".format(x)
            print("fracaso en ", niter, " iteraciones ")
            mensaje = "fracaso en " + str(niter) + " iteraciones"
            return None, mensaje
        
        
    def RaicesMultiplesRel(f, df1, df2, x0, tol, niter):
        f = InputFixed.CorregirFuncion(f)
        df1 = InputFixed.CorregirFuncion(df1)
        df2 = InputFixed.CorregirFuncion(df2)
        solucion = 0
        x = x0
        fx = eval(f)
        df1x = eval(df1)
        df2x = eval(df2)
        Error = 100
        c = 0
        resultados = []
        resultados.append([c,x,fx,100])
        while Error > tol and c < niter and fx != 0:
            x = x0 - (fx * df1x) / ((df1x**2) - (fx*df2x))
            fx = eval(f)
            df1x = eval(df1)
            df2x = eval(df2)

            c = c + 1
            Error = abs((x - x0)/x)
            resultados.append([c,"{:.3e}".format(x),"{:.3e}".format(fx),"{:.3e}".format(Error)])

            x0 = x

        if fx == 0:
            solucion = "{:.5e}".format(x)
            mensaje = str(solucion) + " es raiz de f(x)"
            return resultados, mensaje
        elif Error <= tol:
            solucion = "{:.5e}".format(x)
            mensaje = str(solucion) + " es una aproximacion de un raiz de f(x) con una tolerancia " + str(tol)
            print(f)
            print(df1)
            return resultados, mensaje
        else:
            solucion = "{:.5f}".format(x)
            print("fracaso en ", niter, " iteraciones ")
            mensaje = "fracaso en " + str(niter) + " iteraciones"
            return None, mensaje