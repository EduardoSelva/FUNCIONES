#Eduardo Selva
#Profe, para serle honesto ocupe ayuda de una IA, pero entiendo cómo es la lógica del ejercicio.
print("***** Inventario mínimo *****")
Moneda = "C$"
Iva = 0.15
def agregar_producto(inventario, producto, precio):
    inventario.append([producto, precio])
    return inventario
#Esta función agrega los valores de producto y precio a la lista de inventario y luego las retorna
def calcular_valor_total(inventario):
    resultado = 0

    for producto in inventario:
        resultado = resultado + producto[1]

    resultado = resultado + (resultado * Iva)
    return resultado
# Entiendo que aqui se hace un ciclo para saber el valor total de los productos sumados y luego se le suma el iva correspondiente.
def mostrar_inventario(inventario):
    print("Inventario:")
    
    for producto in inventario:
        print(producto[0], Moneda, producto[1])
# Y en esta parte ya se hace el ciclo para mostrar los productos individualmente con su precio.
inventario = []
inventario = agregar_producto(inventario, "Arroz", 50)
inventario = agregar_producto(inventario, "Frijoles", 40)
inventario = agregar_producto(inventario, "Aceite", 80)
# Aqui se agregan los datos a la lista del inventario con los parametros correctos.
mostrar_inventario(inventario)
total = calcular_valor_total(inventario)
print("Valor total con IVA:", Moneda, total)
#Y esto ultimo, simplemente es la llamada a las funciones para mostrar el inventario y calcular el valor total con IVA.
#Me gustaría que explicara un ejercicio similar en clase, se me hace un poco confuso el tema de las listas y funciones, pero con este ejemplo lo entendí mejor.