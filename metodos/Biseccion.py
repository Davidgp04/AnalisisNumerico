from math import *

class Biseccion:
	def biseccion(f,a,b,tol,niter):
		solucion = 0
		resultados = []
		E = []
		fm = []
		iteraciones = []
		valoresX = []
		x = a
		fa = eval(f)
		x = b
		fb = eval(f)
		c = 0
		iteraciones.append(1)
		if fa == 0:
			solucion = a
			E = 0
			print(a, "es raiz de f(x)")
		elif fb == 0:
			solucion = b
			E = 0
			print(b, "es raiz de f(x)")
		elif fa*fb < 0:
			i = 0
			Error = 100
			Xm = (a+b)/2
			x = Xm
			fx = eval(f)
			fm.append(fx)
			E.append(Error)
			iteraciones.append(1)
			valoresX.append(Xm)
			resultados.append([1,a,Xm,b,fx,100])
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
				fm.append(fx)
				Error = abs(Xm - Xtemp)
				E.append(Error)
				valoresX.append(Xm)
				c = c + 1
				iteraciones.append(c+1)
				resultados.append([c+1,a,Xm,b,fx,"{:.2e}".format(Error)])

			if fx == 0:
				solucion = x
				print(solucion, "es raiz de f(x)")
				'''print("iteraciones",iteraciones)
				print("valores de x", valoresX)
				print("Fm",fm)
				print("Error",E)'''
				print(resultados)
				return resultados
			elif Error<tol:
				solucion = x
				print(solucion,"es una aproximacion de un raiz de f(x) con una tolerancia", tol)
				'''print("iteraciones",iteraciones)
				print("valores de x", valoresX)
				print("Fm",fm)
				print("Error",E)'''
				print(resultados)
				return resultados
			else:
				solucion = x
				print("Fracaso en ",niter, " iteraciones ") 
				return resultados
		else:
			print("El intervalo es inadecuado")
			return []

#biseccion("x**3-x-1",-1,5,0.5e-7,100)
#biseccion("log(sin(x)**2+1)-(1/2)",0,1,0.5e-7,100)

