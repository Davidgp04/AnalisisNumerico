
class InputFixed:
    def CorregirFuncion(inputString):
        NuevoString = inputString
        if "cos" in inputString:
            NuevoString = NuevoString.replace("cos(", "np.cos(")
        if "sin" in inputString:
            NuevoString = NuevoString.replace("sin(", "np.sin(")
        if "tan" in inputString:
            NuevoString = NuevoString.replace("tan(", "np.tan(")
        if "log" in inputString:
            NuevoString = NuevoString.replace("log(", "np.log(")
        if "exp" in inputString:
            NuevoString = NuevoString.replace("exp(", "np.exp(")
        if "^" in inputString:
            NuevoString = NuevoString.replace("^", "**")
        return NuevoString
    print(CorregirFuncion("cos(x^2)"))