numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))

if numero1 > numero2:
    print (f'O maior numero é: {numero1}')
elif numero2 > numero1:
    print (f'O maior numero é:{numero2}')
elif numero1 == numero2:
    print("Os valores são iguais")
else:
    print("Numeros invalidos")