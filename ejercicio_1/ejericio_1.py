# prgorama que reconozca en que parte del plano cartesiano se encuentran las coorenadas
print("-------------------------------")
print("---------coordenadas-----------")
print("-------------------------------")

# input 
x = int(input("Ingrese la coordenada x del punto: "))
y = int(input("Ingrese la coordenada y del punto: "))

# procesing and output
if x > 0 and y > 0:
    print("El punto está en el primer cuadrante")
elif x < 0 and y > 0:
    print("El punto está en el segundo cuadrante")
elif x < 0 and y < 0:
    print("El punto está en el tercer cuadrante")
elif x > 0 and y < 0:
    print("El punto está en el cuarto cuadrante")
elif x == 0 and y == 0:
    print("El punto está en el origen")
elif x == 0:
    print("El punto está sobre el eje Y")
elif y == 0:
    print("El punto está sobre el eje X")

print("-------------------------------")
print("--------------fin--------------")
print("-------------------------------")



