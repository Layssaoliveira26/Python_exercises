#Objetivo: Receber o nome do usuário e suas 3 notas. Por fim, imprimir o nome do usuário e a média
nome = input("Digite seu nome: ")
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))
media = nota1 + nota2 + nota3 / 3
print("Nome do aluno: ", nome)
print(f"Média do aluno: {media:.2f}" )
