numero_dias = int(input("Digite o número de dias trabalhados: "))

preco_dia = 180.00

gasto_por_dia = numero_dias * preco_dia

imposto = gasto_por_dia * 0.08

valor_final = gasto_por_dia - imposto

print(f'O valor bruto é de R$ {gasto_por_dia:.2f}')
print(f'O imposto é de R$ {imposto:.2f}')
print(f'O valor final é de R$ {valor_final:.2f}')