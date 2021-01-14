import math

def EcuacionCuadratica(a, b, c):
    x1 =  (- b - math.sqrt(b**2 - 4*a*c))/2*a
    x2 =  (- b + math.sqrt(b**2 - 4*a*c))/2*a
    print(f"X1 = {round(x1,0)}")
    print(f"X2 = {round(x2,0)}")
    return x1, x2 

def suma(numero1, numero2):
    suma = numero1 + numero2
    print (f"La suma es: {suma}")
    return suma