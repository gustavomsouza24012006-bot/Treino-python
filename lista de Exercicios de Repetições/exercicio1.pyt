nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

media = (nota1 + nota2 + nota3)/3

if media >= 6:
    print(f'Aluno aprovado com a media: {media}')
else:
    print(f'Aluno reprovado com a media: {media}')
