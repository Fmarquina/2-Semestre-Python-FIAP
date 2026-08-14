import os
os.system("cls")

# Dicionario com listas
aluno = {
    "nome": "Ana",
    #          0    1    2
    "notas": [5.5, 6.0, 9.5],
}

print(aluno["nome"])
#print(aluno["notas"][1])

for nota in aluno["notas"]:
    print(f"Nota: {nota}")