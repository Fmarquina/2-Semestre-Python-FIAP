import os
os.system("cls")

# Lista de diccionarios
alunos =[
    {
        "nome": "Ana",
        "idade": 18,
    },
    {
        "nome": "Carlos",
        "idade": 44,
    }
]
print(alunos)

aluno={
    'nome': '',
    'idade': 0
}
aluno["nome"] = input("Nome: ")
aluno["idade"] = int(input("Idade: "))

alunos.append(aluno)

print(alunos)