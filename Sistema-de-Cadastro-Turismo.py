#biblioteca importada
import time

#lista que será usada para organizar os clientes registrados
cadastros = []
#lista com o nome e preços das viagens disponiveis
viagens = [
    "Santos ---------------- R$500,00",
    "Fernando de Noronha --- R$850,00",
    "Recife ---------------- R$650,00",
    "Maceió ---------------- R$550,00",
    "Rio de Janeiro -------- R$700,00",
    "Miami Beach ----------- R$1250,00"
]
print("Seja Bem-Vindo(a) ao EcoSail Soluções!")

#função usada para ativar um delay de 1 segundo para continuar o resto do codigo
time.sleep(1)

#função criada para registrar o nome de um cliente novo
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
        #listando as opções disponiveis para o ciente
        print("""
1 - Cadastrar Cliente.
2 - Verificar Clientes.
3 - Remover Cente.
4 - Registrar Viagem.
5 - Sair.
""")
        #Criando uma variavel para definir a opção escolhida pelo cliente
        opcao = int(input("Escolha uma opção: "))

        match opcao:

            case 1: #ao digitar 1 o codigo ira ativar a função de registrar um cliente, e logo em seguida colocando ele na lista de cadastros
                cliente_novo = get_cadastro()
                cadastros.append(cliente_novo)
            case 2: #verifica se a lista de clientes está vazia, se não ele lista todos os nomes na lista de cadastros
                if not len(cadastros) == 0:
                    for i in cadastros:
                        print(i)
                else:
                    print("Nenhum cliente foi adicionado.")
            case 3: #remove um nome da lista de cadastros
                remover = input("Qual Cliente deseja remover? ")
                cadastros.remove(remover)
                print(f"Cliente {remover} removido com sucesso!")
            case 4: #lista as viagens disponiveis para o cliente
                print("Viagens disponíveis:")
                for indice, viagem in enumerate(viagens):
                    print(f"{(indice + 1)} - {viagem}")

                #pede para o usuario escolher uma das opções para realizar o pagamento da viagem
                escolher_viagem = int(input("Escolha uma das opções(Digite o número da viagem): "))

                match escolher_viagem:
                    #faz o pagamento com pix e limpa a lista do cadastro para poder realizar outra viagem se desejado
                    case 1:
                        print("")
                        print("Viagem selecionada: Santos")
                        print("Preço Total: R$500,00")
                        print("Clientes registrados:")
                        for i in cadastros:
                            print(i)
                        confirmar = str(input("Pagar com PIX?(Sim ou Não) "))
                        if confirmar.upper() == "SIM":
                            print("Código PIX(CNPJ): 92.958.800/0001-38")
                            cadastros.clear()
                        else:
                            print("Pagamente cancelado!")
                            break
                    case 2:
                        print("")
                        print("Viagem selecionada: Fernando de Noronha")
                        print("Preço Total: R$850,00")
                        print("Clientes Registrados:")
                        for i in cadastros:
                            print(i)
                        confirmar = str(input("Pagar com PIX?(Sim ou Não) "))
                        if confirmar.upper() == "SIM":
                            print("Código PIX(CNPJ): 92.958.800/0001-38")
                            cadastros.clear()
                        else:
                            print("Pagamente cancelado!")
                            break
                    case 3:
                        print("")
                        print("Viagem selecionada: Recife")
                        print("Preço Total: R$650,00")
                        print("Clientes Registrados:")
                        for i in cadastros:
                            print(i)
                        confirmar = str(input("Pagar com PIX?(Sim ou Não) "))
                        if confirmar.upper() == "SIM":
                            print("Código PIX(CNPJ): 92.958.800/0001-38")
                            cadastros.clear()
                        else:
                            print("Pagamente cancelado!")
                            break
                    case 4:
                        print("")
                        print("Viagem selecionada: Maceió")
                        print("Preço Total: R$550,00")
                        print("Clientes Registrados:")
                        for i in cadastros:
                            print(i)
                        confirmar = str(input("Pagar com PIX?(Sim ou Não) "))
                        if confirmar.upper() == "SIM":
                            print("Código PIX(CNPJ): 92.958.800/0001-38")
                            cadastros.clear()
                        else:
                            print("Pagamente cancelado!")
                            break
                    case 5:
                        print("")
                        print("Viagem selecionada: Rio de Janeiro")
                        print("Preço Total: R$700,00")
                        print("Clientes Registrados:")
                        for i in cadastros:
                            print(i)
                        confirmar = str(input("Pagar com PIX?(Sim ou Não) "))
                        if confirmar.upper() == "SIM":
                            print("Código PIX(CNPJ): 92.958.800/0001-38")
                            cadastros.clear()
                        else:
                            print("Pagamente cancelado!")
                            break
                    case 6:
                        print("")
                        print("Viagem selecionada: Miami Beach")
                        print("Preço Total: R$1250,00")
                        print("Clientes Registrados:")
                        for i in cadastros:
                            print(i)
                        confirmar = str(input("Pagar com PIX?(Sim ou Não) "))
                        if confirmar.upper() == "SIM":
                            print("Código PIX(CNPJ): 92.958.800/0001-38")
                            cadastros.clear()
                        else:
                            print("Pagamente cancelado!")
                            break
            case 5: #finalza o programa
                print("Obrigado por usar o nosso programa de cadastro!")
                break

main()
