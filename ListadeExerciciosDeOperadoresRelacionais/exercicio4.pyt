votos_branco = int(input("Digite o número de votos brancos: "))
votos_nulo = int(input("Digite o número de votos nulos: "))
votos_validos = int(input("Digite o número de votos válidos: "))

total_votos = votos_branco + votos_nulo + votos_validos

porcentagem_brancos = (votos_branco / total_votos) * 100
porcentagem_nulos = (votos_nulo / total_votos) * 100
porcentagem_validos = (votos_validos / total_votos) * 100

print(f"Porcentagem de votos brancos: {porcentagem_brancos:.2f}%")
print(f"Porcentagem de votos nulos: {porcentagem_nulos:.2f}%")
print(f"Porcentagem de votos válidos: {porcentagem_validos:.2f}%")