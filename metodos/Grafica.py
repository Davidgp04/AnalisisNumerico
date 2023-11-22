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
    
    def GraficarPolinomio(f, xmin, xmax, ymin, ymax):       
        RangoX = np.linspace(-25,25,1000)
        x = RangoX
        RangoY = eval(f)

        fig, ax = plt.subplots()
        ax.plot(x, RangoY,zorder = 1, color = 'green')
        ax.set_xlim(xmin, xmax)
        ax.set_ylim(ymin, ymax)
        # Dibujar la línea horizontal en y = 0
        ax.axhline(y=0, color='black', label='y = 0',zorder = 0)
        
        # Dibujar la línea vertical en x = 0
        ax.axvline(x=0, color='black', label='x = 0',zorder = 0)
        
        imgdata = StringIO()
        fig.savefig(imgdata, format='svg')
        imgdata.seek(0)
        data = imgdata.getvalue()
        return data
    
    def GraficarFunciones(funciones, xmin, xmax, ymin, ymax):
        RangoX = np.linspace(xmin, xmax, 1000)
        x = RangoX
        
        fig, ax = plt.subplots()

        # Definir una lista de colores
        colores = ['blue', 'green', 'red', 'purple', 'orange', 'brown', 'pink', 'gray', 'olive', 'cyan']
        
        # Iterar sobre la lista de funciones y graficar cada una con un color diferente
        for i, f in enumerate(funciones):
            RangoY = eval(f)
            ax.plot(x, RangoY, color=colores[i % len(colores)], zorder=1, label=f)

        ax.set_xlim(xmin, xmax)
        ax.set_ylim(ymin, ymax)

        # Dibujar las líneas horizontales y verticales para los ejes
        ax.axhline(y=0, color='black', label='y = 0', zorder=0)
        ax.axvline(x=0, color='black', label='x = 0', zorder=0)

        imgdata = StringIO()
        fig.savefig(imgdata, format='svg')
        imgdata.seek(0)
        data = imgdata.getvalue()
        return data