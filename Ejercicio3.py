#Eduardo Selva
print("*** Variables repetidas ***")
print("-------- Función: Suma --------")
def suma():
    resultado = 10 + 5
    return resultado
print("Resultado de la suma:", suma())
print("-------- Función: Resta --------")
def resta():
    resultado = 20 - 8
    return resultado
print("Resultado de la resta:", resta())
print("-------- Función: Multiplicación --------")
def multiplicacion():
    resultado = 4 * 3
    return resultado
print("Resultado de la multiplicación:", multiplicacion())
print("***************************")
#Aunque todas las funciones lleven la variable "Resultado", no conflictuan ya que cada resultado es una variable local de su función.