nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
faltas = int(input("Digite o numero de faltas"))

media = (nota1 + nota2) / 2

if media > 6.0 and faltas < 20 :
    print(f'Aluno aprovado com a media: {media} ')

else:
    print(f'Aluno reprovado com a media: {media}  e faltas {faltas}')

