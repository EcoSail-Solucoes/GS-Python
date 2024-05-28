#bibliotecas importadas
import time

cadastros = []
viagens = []
print("Seja Bem-Vindo(a) ao EcoSail Soluções!")
time.sleep(1)
print("""
1 - Cadastrar Cliente.
2 - Verificar Clientes.
3 - Remover Cliente.
4 - Viagens.
5 - Registrar Viagem.
6 - Listar viagens registradas.
7 - Confirmar.
8 - Sair.
""")
def get_cadastro():
    while True:
        cadastro = input("Nome do cliente: ")
        if not cadastro.isdigit():
            print("Cliente registrado com sucesso!")
            return cadastro
        else:
            print("Digite um nome válido.")
def main():
    while True:
        opcao = int(input("Escolha uma opção: "))
        match opcao:
            case 1:
                cliente_novo = get_cadastro()
                cadastros.append(cliente_novo)
            case 2:
                if not len(cadastros) == 0:
                    for i in cadastros:
                        print(i)
                else:
                    print("Nenhum cliente foi adicionado.")
            case 3:
                remover = input("Qual Cliente deseja remover? ")
                cadastros.remove(remover)
            # case 4:
            #
            # case 5:
            #
            case 6:
                break

main()
