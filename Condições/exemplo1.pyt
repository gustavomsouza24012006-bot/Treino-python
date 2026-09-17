valor = float(input("O valor da compra: "))

if valor > 300:
    print("Aplicando desconto de 10%")
    valor = valor * 0.90

print(f'Valor Atualizado: R${valor:.2f}')
