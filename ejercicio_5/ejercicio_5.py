print("-------------------------")
print("------costo de agua------")
print("-------------------------")


# input
m3_gastados = float(input("Ingrese el número de m3 de agua gastados: "))

# procesing
if m3_gastados <= 50:
    costo_total = 10000  
elif m3_gastados <= 200:
    costo_total = 10000 + (m3_gastados - 50) * 2000
else:
    costo_total = 10000 + (150 * 2000) + (m3_gastados - 200) * 3000

# output
print("El costo total de agua es de: "+str(costo_total))