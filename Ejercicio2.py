#Eduardo Selva
print("*** Modificación del caso 4 ***")
print("---------Usando Global----------")
saldo = 500
def retirar(monto):
    global saldo
    saldo = saldo - monto
    return saldo
print("Ha retirado C$",retirar(100))
print("--------Usando Return----------")
saldo = 500
def retirar(saldo, monto):
    saldo = saldo - monto
    return saldo
saldo = retirar(saldo, 100)
print(f"ha retirado C${saldo}")
print("****************************")
#Prefiero usar el return, es más exacto.
