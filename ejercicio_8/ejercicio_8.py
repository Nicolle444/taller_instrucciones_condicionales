print("-----------------------------")
print("----dos enteros multiplos----")
print("-----------------------------")

# input
a = int(input("Ingrese el primer número entero: "))
b = int(input("Ingrese el segundo número entero: "))

# procesing and output
if a % b == 0:
    print(a, "es múltiplo de", b)
elif b % a == 0:
    print(b, "es múltiplo de", a)
else:
    print("Los números no son múltiplos entre sí.")

print("-----------------------------")
print("-------------fin-------------")
print("-----------------------------")