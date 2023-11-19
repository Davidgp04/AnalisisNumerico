import matplotlib.pyplot as plt
import numpy as np
from math import *
from io import StringIO
from metodos.InputFixed import InputFixed

class Grafica:
    def Graficar(f):
        try:
            if(f == ''):
                return None
            else:
                RangoX = np.linspace(-25,25,1000)
                x = RangoX
                RangoY = eval(f)
                fig, ax = plt.subplots()
                ax.plot(x, RangoY,zorder = 1, color = 'green')
                ax.set_xlim(-25, 25)
                ax.set_ylim(-25, 25)
                # Dibujar la línea horizontal y vertical en 0
                ax.axhline(y=0, color='black', label='y = 0',zorder = 0)
                ax.axvline(x=0, color='black', label='x = 0',zorder = 0)
                imgdata = StringIO()
                fig.savefig(imgdata, format='svg')
                imgdata.seek(0)
                data = imgdata.getvalue()
                return data
        except: 
            return("No se puede graficar esta funcion")
        
    def GraficarSolucion(f,posX):
        try:
            f = InputFixed.CorregirFuncion(f)
            RangoX = np.linspace(-25,25,1000)
            x = RangoX
            RangoY = eval(f)
            fig, ax = plt.subplots()
            ax.plot(x, RangoY,zorder = 1, color = 'green')
            ax.set_xlim(posX-15, posX+15)
            ax.set_ylim(-25, 25)
            # Dibujar la línea horizontal y vertical en 0
            ax.axhline(y=0, color='black', label='y = 0',zorder = 0)
            ax.axvline(x=0, color='black', label='x = 0',zorder = 0)
            imgdata = StringIO()
            fig.savefig(imgdata, format='svg')
            imgdata.seek(0)
            data = imgdata.getvalue()
            return data
        except: 
            return("No se puede graficar esta funcion")