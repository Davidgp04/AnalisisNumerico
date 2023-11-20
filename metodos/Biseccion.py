from math import *
import numpy as np
class Biseccion:
    
	def biseccion(f,a,b,tol,niter):
		solucion = 0
		resultados = []
		x = a
		fa = eval(f)
		x = b
		fb = eval(f)
		c = 0
		if fa == 0:
			solucion = a
			mensaje = str(solucion) + " es raiz de (f)"
			return None, mensaje
		elif fb == 0:
			solucion = b
			mensaje = str(solucion) + " es raiz de (f)"
			return None, mensaje
		elif fa*fb < 0:
			i = 0
			Error = 100
			Xm = (a+b)/2
			x = Xm
			fx = eval(f)
			resultados.append([1,a,Xm,b,"{:.3e}".format(fx),100])
			while Error > tol and fx != 0 and i < niter:
				if fx * fa < 0:
					b = Xm
					x = b
					fb = eval(f)
				else:
					a = Xm
					x = a
					fb = eval(f)
				Xtemp = Xm
				Xm = (a+b)/2
				x = Xm
				fx = eval(f)
				Error = abs(Xm - Xtemp)
				c = c + 1
				resultados.append([c+1,"{:.5f}".format(a),"{:.5f}".format(Xm),"{:.5f}".format(b),"{:.3e}".format(fx),"{:.3e}".format(Error)])

			if fx == 0:
				solucion = "{:.5f}".format(x)
				mensaje = str(solucion) + " es raiz de f(x)"
				return resultados, mensaje, solucion
			elif Error<tol:
				solucion = "{:.5f}".format(x)
				mensaje = str(solucion) + " es una aproximacion de un raiz de f(x) con una tolerancia " + str(tol)
				return resultados, mensaje, solucion
			else:
				solucion = "{:.5f}".format(x)
				mensaje = "Fracaso en " + str(niter) + " iteraciones"
				return resultados, mensaje, None
		else:
			mensaje = "El intervalo es inadecuado"
			return None, mensaje, None

	def biseccionRel(f,a,b,tol,niter):
		solucion = 0
		resultados = []
		x = a
		fa = eval(f)
		x = b
		fb = eval(f)
		c = 0
		if fa == 0:
			solucion = a
			mensaje = str(solucion) + " es raiz de (f)"
			return None, mensaje
		elif fb == 0:
			solucion = b
			mensaje = str(solucion) + " es raiz de (f)"
			return None, mensaje
		elif fa*fb < 0:
			i = 0
			Error = 100
			Xm = (a+b)/2
			x = Xm
			fx = eval(f)
			resultados.append([1,a,Xm,b,"{:.3e}".format(fx),100])
			while Error > tol and fx != 0 and i < niter:
				if fx * fa < 0:
					b = Xm
					x = b
					fb = eval(f)
				else:
					a = Xm
					x = a
					fb = eval(f)
				Xtemp = Xm
				Xm = (a+b)/2
				x = Xm
				fx = eval(f)
				Error = abs((Xm - Xtemp)/Xm)
				c = c + 1
				resultados.append([c+1,"{:.5f}".format(a),"{:.5f}".format(Xm),"{:.5f}".format(b),"{:.3e}".format(fx),"{:.3e}".format(Error)])
			if fx == 0:
				solucion = "{:.5f}".format(x)
				mensaje = str(solucion) + " es raiz de f(x)"
				return resultados, mensaje, solucion
			elif Error<tol:
				solucion = "{:.5f}".format(x)
				mensaje = str(solucion) + " es una aproximacion de un raiz de f(x) con una tolerancia " + str(tol)
				return resultados, mensaje, solucion
			else:
				solucion = "{:.5f}".format(x)
				mensaje = "Fracaso en " + str(niter) + " iteraciones"
				return resultados, mensaje, None
		else:
			mensaje = "El intervalo es inadecuado"
			return None, mensaje, None