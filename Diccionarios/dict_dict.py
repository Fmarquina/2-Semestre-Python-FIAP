import os
os.system("cls")

#dicionario de dicionarios
alunos ={
    "RM001" :{
        "nome": "Ana",
        "idade": 44,
    },
    "RM002": {
        "nome": "Jose",
        "idade": 22
    }
}

#print(alunos["RM001"]["idade"])
#print(alunos["RM002"]["nome"])



for rm, dados in alunos.items():
    print(f"RM: {rm}")
    for k in dados.keys():
        print(f"{k.capitalize()}: {dados[k]}")
    print()
    #print(f"Nome: {dados['nome']}")
    #print(f"Idade: {dados['idade']}\n")