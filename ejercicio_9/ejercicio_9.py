# programa para saber si un triangulo es agudo, recto o obvtuso



# input
a = float(input("Ingrese la longitud del lado a: "))
b = float(input("Ingrese la longitud del lado b: "))
c = float(input("Ingrese la longitud del lado c: "))


# procesing and outoput
if a >= b + c or b >= a + c or c >= a + b:
    print("No es un triángulo válido")
elif a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
    print("El triángulo es recto")
elif a**2 > b**2 + c**2 or b**2 > a**2 + c**2 or c**2 > a**2 + b**2:
    print("El triángulo es obtuso")
else:
    print("El triángulo es agudo")