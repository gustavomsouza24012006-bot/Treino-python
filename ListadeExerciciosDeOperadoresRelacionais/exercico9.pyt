comprimento = float(input("Digite o comprimento da cozinha: "))
largura = float(input("Digite a largura da cozinha: "))
altura = float(input("Digite a altura da cozinha: "))

area_paredes = (2 * comprimento * altura) + (2 * largura * altura)

caixas = area_paredes / 1.5

print(f"A área total das paredes é: {area_paredes:.2f} m²")
print(f"A quantidade de caixas necessárias é: {caixas:.2f}")