import json

arquivo_tarefas = 'to_do.json'

try:
    with open(arquivo_tarefas, 'r') as arquivo:
        lista_tarefas = json.load(arquivo)
except FileNotFoundError:
    lista_tarefas = []

def salvar_tarefas():
    with open(arquivo_tarefas, 'w') as arquivo:
        json.dump(lista_tarefas, arquivo)

def exibir_tarefas():
    print("\n***Lista de Tarefas:  ")
    for i, tarefa in enumerate(lista_tarefas, start=1):
        print(f"({i}) - {tarefa}")

while True:
    print("\n***Opções:  ")
    print("1. Adicionar Tarefa")
    print("2. Exibir Tarefas")
    print("3. Remover Tarefa")
    print("4. Sair")

    escolha = int(input())

    if(escolha == 1):
        tarefa_nova = input("Digite a nova tarefa: \n")
        lista_tarefas.append(tarefa_nova)
        print(f"Tarefa: {tarefa_nova}, adicionada com sucesso!")
    elif(escolha == 2):
        exibir_tarefas()
        if(lista_tarefas == []):
            print("Você não tem tarefas registradas!")
    elif(escolha == 3):
        exibir_tarefas()
        numero_tarefa = int(input("Digite o número da tarefa a ser removida.\n"))
        if(1 <= numero_tarefa <= len(lista_tarefas)):
            tarefa_removida = lista_tarefas.pop(numero_tarefa -1)
            print(f"Tarefa '{tarefa_removida}' removida com sucesso!")
        else:
            print("Número de tarefa inválido!")
    elif(escolha == 4):
        print("Saindo do programa. Até logo!")
        salvar_tarefas()
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")