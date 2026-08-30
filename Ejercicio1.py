#Eduardo Selva
print("*** Tasa de cambio dólar-Córdoba ***")
TasaDeCambio = 36.6
def a_dolares(cordobas):
    dolares = cordobas / TasaDeCambio   
    return dolares
print(round(a_dolares(100), 2))
print(dolares)
print("***************************")
#El error que muestra es "NameError: name 'dolares' is not defined. Did you mean: 'a_dolares'?"
#Esto porque la variable "dolares" es una variable local y no se puede usar fuera de la función