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
print("""
1 - Cadastrar Cliente.
2 - Verificar Clientes.
3 - Remover Cliente.
4 - Registrar Viagem.
5 - Sair.
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
                print(f"Cliente {remover} removido com sucesso!")
            case 4:
                print("Viagens disponíveis:")
                for indice, viagem in enumerate(viagens):
                    print(f"{(indice + 1)} - {viagem}")
                escolher_viagem = int(input("Escolha uma das opções(Digite o número da viagem): "))
                match escolher_viagem:
                    case 1:
                        print("Preço Total: R$500,00")
                        print("Clientes registrados:")
                        for i in cadastros:
                            print(i)
                        confirmar = str(input("Pagar com PIX?(Sim ou Não) "))
                    case 2:
                        print("Preço Total: R$850,00")
                        print(f"Clientes registrados: {cadastros}")
                        confirmar = str(input("Pagar com PIX?(Sim ou Não) "))
                    case 3:
                        print("Preço Total: R$650,00")
                        print(f"Clientes registrados: {cadastros}")
                        confirmar = str(input("Pagar com PIX?(Sim ou Não) "))
                    case 4:
                        print("Preço Total: R$550,00")
                        print(f"Clientes registrados: {cadastros}")
                        confirmar = str(input("Pagar com PIX?(Sim ou Não) "))
                    case 5:
                        print("Preço Total: R$700,00")
                        print(f"Clientes registrados: {cadastros}")
                        confirmar = str(input("Pagar com PIX?(Sim ou Não) "))
                    case 6:
                        print("Preço Total: R$1250,00")
                        print(f"Clientes registrados: {cadastros}")
                        confirmar = str(input("Pagar com PIX?(Sim ou Não) "))
            case 5:
                print("Obrigado por usar o nosso programa de cadastro!")
                break

main()
