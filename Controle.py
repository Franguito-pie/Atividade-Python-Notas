#SISTEMA DE CONTROLE DE NOTAS

n = 1
ap = 0
rp = 0
rec = 0
aluno = 0

print("Bem vindo ao sistema de cadastro de notas! Segue os comandos abaixo: \n")

while n == 1:
    print("==========================CONTROLE DE NOTAS==========================")
    print("1 - Cadastrar notas de um aluno -------------------------------------")
    print("2 - Mostrar quantidades de alunos cadastrados -----------------------")
    print("3 - Mostrar quantidade de aprovados ---------------------------------")
    print("4 - Mostrar quantidade de recuperação -------------------------------")
    print("5 - Mostrar quantidade de reprovados --------------------------------")
    print("6 - Encerrar --------------------------------------------------------")

    p = int(input("\nDigite o número do comando: "))

    if p == 1:
        aluno += 1
        nota1 = int(input("\nDigite a primeira nota: "))
        nota2 = int(input("Digite a segunda nota: "))
        media = (nota1 + nota2) / 2

        if media >= 7:
            ap += 1
            print("\nAluno cadastrado com sucesso!")

        elif media < 7 and media >= 5:
            rec += 1
            print("\nAluno cadastrado com sucesso!")

        elif media < 5:
            rp += 1
            print("\nAluno cadastrado com sucesso!")

    elif p == 2:
        print(f"\nQuantidade de alunos cadastrados: {aluno}")

    elif p == 3:
        print(f"\nQuantidade de aprovados: {ap}")

    elif p == 4:
        print(f"\nQuantidade de recuperação: {rec}")

    elif p == 5:
        print(f"\nQuantidade de reprovados: {rp}")

    elif p == 6:
        print("\nPrograma encerrado!")
        break

    else:
        print("ERRO!")