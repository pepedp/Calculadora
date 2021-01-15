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

def resta(numero1, numero2):
    resta = numero1 - numero2
    print (f"La resta es: {resta}")
    return resta

# Funcion para la multiplicaicon de 2 numeros 
def multiplicacion(numero1, numero2):
    multiplicacion = numero1 * numero2
    print (f"La muliplicacion es: {multiplicacion}")
    return multiplicacion

# Funcion para la division de 2 numeros 
def division(numero1, numero2):
    division = numero1 / numero2
    print (f"La division es: {round(division,2)}")
    return division