#bibliotecas importadas
import time

cadastros = []
viagens = [
    "Santos ---------------- R$500,00",
    "Fernando de Noronha --- R$850,00",
    "Recife ---------------- R$650,00",
    "Maceió ---------------- R$550,00",
    "Rio de Janeiro -------- R$700,00",
    "Miami Beach ----------- R$1250,00"
]
print("Seja Bem-Vindo(a) ao EcoSail Soluções!")
time.sleep(1)
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
        print("""
1 - Cadastrar Cliente.
2 - Verifliicar Clientes.
3 - Remover Cente.
4 - Registrar Viagem.
5 - Sair.
""")
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
                print(f"Cliente {remover} removido com sucesso!")
            case 4:
                print("Viagens disponíveis:")
                for indice, viagem in enumerate(viagens):
                    print(f"{(indice + 1)} - {viagem}")
                escolher_viagem = int(input("Escolha uma das opções(Digite o número da viagem): "))
                match escolher_viagem:
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
            case 5:
                print("Obrigado por usar o nosso programa de cadastro!")
                break

main()
