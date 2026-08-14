import os
os.system("cls")

# 1. Fazer um procedimento que permita ao usuário preencher o diccionario aluno.
def preencher(a: dict) -> None:
    print("---------------------")
    a['nome'] = input("Nome: ")
    a['idade'] = int(input("Idade: "))
    a['curso'] = input("Curso: ")

# 2. Fazer um procedimento que exiba o diccionário aluno.
def exibir(a: dict) -> None:
    print("---------------------")
    for k, v in a.items():
        print(f"{k.title()}: {v}")

# 3. Fazer uma função que conte quantas keys há no diccionário.
def contar_keys(a: dict) -> int:
    return len(a.keys())

aluno = {
    'nome': 'Marcelo',
    'idade': '34',
    'curso': 'TDS'
}

exibir(aluno)
#print(aluno)
preencher(aluno)
print(aluno)
print("Quantidade de keys: ", contar_keys(aluno))

"""
EXERCICIOS:
1. Fazer um procedimento que permita ao usuário preencher o diccionario aluno.
2. Fazer um procedimento que exiba o diccionário aluno.
3. Fazer uma função que conte quantas keys há no diccionário.
"""

