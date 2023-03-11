print("-----------------------------")
print("-----préstamo bancario-------")
print("-----------------------------")

# input
ingresos = int(input("Ingrese el valor de sus ingresos: "))
deuda = int(input("Ingrese el valor total de sus deudas: "))

# procesing and output
if ingresos > 945200 and deuda == 0:
    print("si cumple con las condiciones para solicitar el préstamo")
else:
    print("no cumple, ni puede realizar el préstamo")


print("-----------------------------")
print("-------------fin-------------")
print("-----------------------------")

