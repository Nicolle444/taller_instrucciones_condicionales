# Programa que calcula el estado de salud de una persona segun su peso y altura
print("-------------------------------")
print("--------estado de salud--------")
print("-------------------------------")

# input
peso =float(input("Ingrese su peso actual en Kg: "))
altura =float(input("Ingrese su altura actual en metros: "))

# procesing and output
IMC = peso // (altura ** 2)
if IMC < 16:
    print("su diagnostico es criterio de ingreso en hospital")
elif IMC > 16 and IMC < 17:
    print("su diagnostico es infrapeso")
elif IMC > 17 and IMC < 18:
    print("su diagnostico es bajo peso")
elif IMC > 18 and IMC < 25:
    print("su diagnostico es peso normal(saludable)")
elif IMC > 25 and IMC < 30:
    print("su diagnostico es sobrepeso(obesidad grado I)")
elif IMC > 30 and IMC < 35:
    print("su diagnostico es Sobrepeso crónico (obesidad grado II)")
elif IMC > 35 and IMC < 40:
    print("Obesidad premórbida (obesidad grado III)")
elif IMC > 40:
    print("Obesidad mórbida (obesidad de grado IV)")
