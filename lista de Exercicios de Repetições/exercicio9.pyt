lado1 = float(input("Digite o lado 1: "))
lado2 = float(input("Digite o lado 2: "))
lado3 = float(input("Digite o lado 3: "))

if lado1 == lado2 == lado3:
    print("equilátero")
elif lado1 == lado2 and lado1 != lado3:
    print("isósceles")
elif lado1!= lado2 != lado3:
    print("escaleno")
else:
    print("erro")