carro = float(input("Digite o valor do carro: "))

custo_impostos = 0.45 * carro
porcentual_distribuidor = 0.28 * carro

preco_final = carro + custo_impostos + porcentual_distribuidor

print(f'O preço final do carro é: R$ {preco_final:.2f} com o custo de impostos de R$ {custo_impostos:.2f} e o percentual do distribuidor de R$ {porcentual_distribuidor:.2f}.')