# programa para calcular la ganancia total de una venta
print("-----------------------------")
print("------ganancias totales------")
print("-----------------------------")

# input
producto =int(input("Ingrese el valor del producto: "))

# procesing
if producto < 3000:
    ganancia = producto * 0.15
elif producto >= 3000 and producto <= 6000:
    ganancia = 500
else:
    ganancia = producto * 0.25
a = ganancia + producto 
# output
print("la ganancia total del producto vendido es: "+str(a))

print("-----------------------------")
print("-----------fin---------------")
print("-----------------------------")
