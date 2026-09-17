salario_fixo = float(input("Digite o seu salario fixo: "))

Valor_vendas = float(input("Digite a valor realizado pelas vendas: "))

if Valor_vendas <= 1500:
    comissao = Valor_vendas * 0.30
    salario_total = salario_fixo + comissao
    print(f'O valor de seu salario é: {salario_total}')

elif Valor_vendas >= 1500:
    comissao = Valor_vendas * 0.50
    salario_total = salario_fixo + comissao
    print(f'O valor de seu salario é: {salario_total}')
else:
    print("erro")