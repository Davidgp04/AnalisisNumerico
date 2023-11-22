class Polinomio:
    
    def crear_polinomio_vander(coeficientes):
        terminos = []
        n = len(coeficientes)
        for i, coef in enumerate(coeficientes):
            if n - i - 1 == 0:
                terminos.append(str(coef))
            elif n - i - 1 == 1:
                terminos.append(f"{coef}*x")
            else:
                terminos.append(f"{coef}*x**{n - i - 1}")
        polinomio = "+".join(terminos)
        return polinomio
    
    def polinomio_newton_string(coef, x_data):
        terminos = ["{:.2f}".format(coef[0])]
        for i in range(1, len(coef)):
            termino = "{:.2f}".format(coef[i]) if coef[i] >= 0 else "{:.2f}".format(coef[i])
            for j in range(i):
                termino += "*(x-{:.2f})".format(x_data[j])
            terminos.append(termino)
        return "+".join(terminos).replace("+-", "-")    
    
    def lagrange_polynomial(x_nodes, y_nodes):
        n = len(x_nodes)
        polynomial = ""
        for i in range(n):
            term = f"{y_nodes[i]}*("
            for j in range(n):
                if i != j:
                    term += f"(x-{x_nodes[j]})*"
            term = term[:-1]+")/("
        for j in range(n):
            if i != j:
                term += f"({x_nodes[i]}-{x_nodes[j]})*"
        term = term[:-1]+")"
        polynomial += term
        if i != n-1:
            polynomial += " + "
        return polynomial.replace('[','').replace(']','').replace('--','+')
    
    def crear_polinomio_spline(coeficientes):
        terminos = []
        n = len(coeficientes)
        for i, coef in enumerate(coeficientes):
            if n - i - 1 == 0:
                terminos.append(str(coef))
            elif n - i - 1 == 1:
                terminos.append(f"{coef}*x")
            else:
                terminos.append(f"{coef}*x**{n - i - 1}")
        polinomio = "+".join(terminos)
        return polinomio.replace("+-","-")