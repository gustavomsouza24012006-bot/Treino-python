numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))
numero3 = float(input("Digite o terceiro numero: "))

if numero1 > numero2 and numero3 < numero1:
    print (f'O maior numero é: {numero1}')
elif numero2 > numero1 and numero2 > numero3:
    print (f'O maior numero é:{numero2}')

elif numero3 > numero1 and numero3 > numero2:
    print (f'O maior numero é:{numero3}')

elif numero1 == numero2 == numero3:
    print("Os valores são iguais")
else:
    print("Numeros invalidos")