import numpy as np
from metodos.InputFixed import InputFixed

class NewtonRaphson:
    def Newton(f,df1,x0,tol,niter):
        f = InputFixed.CorregirFuncion(f)
        df1 = InputFixed.CorregirFuncion(df1)
        solucion = 0
        resultados = []
        x = x0
        fx = eval(f)
        df1x = eval(df1)
        Error = 100
        c = 0
        resultados.append([c,x,"{:.3e}".format(fx),100])

        while Error > tol and c < niter and fx != 0:
            x = x0 - (fx/df1x)
            fx = eval(f)  
            df1x = eval(df1)

            c = c + 1
            Error = abs(x - x0)

            resultados.append([c,"{:.5f}".format(x),"{:.3e}".format(fx),"{:.3e}".format(Error)])

            x0 = x  

        if fx == 0:
            solucion = "{:.5f}".format(x)
            mensaje = str(solucion) + " es raiz de f(x)"
            return resultados, mensaje, solucion
        elif Error <= tol:
            solucion = "{:.5f}".format(x)
            mensaje = str(solucion) + " es una aproximacion de un raiz de f(x) con una tolerancia " + str(tol)
            return resultados, mensaje, solucion
        else:
            solucion = "{:.5f}".format(x)
            mensaje = "fracaso en " + str(niter) + " iteraciones"
            return resultados, mensaje, None
        
        
        
    def NewtonRel(f,df1,x0,tol,niter):
        f = InputFixed.CorregirFuncion(f)
        df1 = InputFixed.CorregirFuncion(df1)
        solucion = 0
        resultados = []
        x = x0
        fx = eval(f)
        df1x = eval(df1)
        Error = 100
        c = 0
        resultados.append([c,x,"{:.3e}".format(fx),100])

        while Error > tol and c < niter and fx != 0:
            x = x0 - (fx/df1x)
            fx = eval(f)  
            df1x = eval(df1)

            c = c + 1
            Error = abs((x - x0)/x)

            resultados.append([c,"{:.5f}".format(x),"{:.3e}".format(fx),"{:.3e}".format(Error)])

            x0 = x  

        if fx == 0:
            solucion = "{:.5f}".format(x)
            mensaje = str(solucion) + " es raiz de f(x)"
            return resultados, mensaje, solucion
        elif Error <= tol:
            solucion = "{:.5f}".format(x)
            mensaje = str(solucion) + " es una aproximacion de un raiz de f(x) con una tolerancia " + str(tol)
            return resultados, mensaje, solucion
        else:
            solucion = "{:.5f}".format(x)
            mensaje = "fracaso en " + str(niter) + " iteraciones"
            return resultados, mensaje, None
