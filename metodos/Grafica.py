import matplotlib.pyplot as plt
import numpy as np
from math import *
from io import StringIO

class Grafica:
    def Graficar(f):
        if(f == ''):
            return None
        else:

            RangoX = np.arange(-5,8,0.1)
            x = RangoX
            RangoY = eval(f)

            fig, ax = plt.subplots()
            ax.plot(x, RangoY)
            ax.set_xlim(-5, 5)
            ax.set_ylim(0, 25)

            imgdata = StringIO()
            fig.savefig(imgdata, format='svg')
            imgdata.seek(0)

            data = imgdata.getvalue()
            return data
