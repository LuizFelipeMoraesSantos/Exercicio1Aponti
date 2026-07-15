nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print(f"A média do aluno é {media}. Aprovado!")

if media >=5 and media < 7:
    print(f"A média do aluno é {media}. Recuperação!")

if media < 5:
    print(f"A média do aluno é {media}. Reprovado!")

