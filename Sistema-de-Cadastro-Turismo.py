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
        cliente = []
        nome = input("Nome do cliente: ")
        if not nome.isdigit():
            cliente.append(nome)
            cpf = input("Digite seu CPF: ")
            cliente.append(cpf)
            telefone = input("Digite seu telefone: ")
            cliente.append(telefone)
            print("Cadastro realizado com sucesso.")
            return cliente
        else:
            print("Digite um nome válido.")

def verificar_cadastros(cliente):
    if not len(cliente) == 0:
        return True
    else:
        return False
    
def destino_viagem(destino):
    while True:
        if destino.upper() == "SANTOS":
            preco = "500,00"
        elif destino.upper() == "FERNANDO DE NORONHA":
            preco = "850,00"
        elif destino.upper() == "RECIFE":
            preco = "650,00"
        elif destino.upper() == "MACEIÓ":
            preco = "550,00"
        elif destino.upper() == "RIO DE JANEIRO":
            preco = "700,00"
        elif destino.upper() == "MIAMI BEACH":
            preco = "1250,00"
        else:
            print("Opção Inválida.")
            break
        resposta = str(input(f'Você escolheu uma viagem com o destino {destino.upper()} por R${preco}, isso está correto?("Sim" ou "Não")'))
        if resposta.upper() == "SIM":
            return True
        elif resposta.upper() == "NÃO" or resposta.upper() == "NAO":
            print("Por favor, confirme sua viagem.")
            return False
        else:
            print("Opção Inválida.")
            continue

def main():
    while True:
        #listando as opções disponiveis para o ciente
        print("""
1 - Cadastrar-se.
2 - Verificar cadastro.
3 - Remover cadastro.
4 - Registrar viagem.
5 - Sair.
""")
        #Criando uma variavel para definir a opção escolhida pelo cliente
        opcao = int(input("Escolha uma opção: "))

        match opcao:

            case 1: #ao digitar 1 o codigo ira ativar a função de registrar um cliente, e logo em seguida colocando ele na lista de cadastros
                cadastros.clear()
                dados_cliente = get_cadastro()
                cadastros.append(dados_cliente)
            case 2: #verifica se a lista de clientes está vazia, se não ele lista todos os nomes na lista de cadastros
                if not len(cadastros) == 0:
                    for i in range(1):
                        for j in range(3):
                            print(cadastros[i][j], end = '\t')
                else:
                    print("Nenhum cliente foi adicionado.")
            case 3: #remove um nome da lista de cadastros
                cadastros.clear()
                print("Cadastro removido com sucesso! Por Favor cadastre um cliente para continuar com a compra.")
            case 4: #lista as viagens disponiveis para o cliente
                if verificar_cadastros(cadastros):
                    print("Viagens disponíveis:")
                    for indice, viagem in enumerate(viagens):
                        print(f"{(indice + 1)} - {viagem}")

                    #pede para o usuario escolher uma das opções para realizar o pagamento da viagem
                    destino = str(input("Escolha uma das opções(Digite o destino da viagem): "))
                    confirmacao_viagem = destino_viagem(destino)
                    if confirmacao_viagem:
                        pagamento = str(input('Deseja pagar com PIX ou Cartão de Débito?(Se a o pagamento for com PIX 20% do valor sera usado para ajudar a limpar as praias que fazem parte da nossa campanha e também ajuda a limpar os oceanos que foram afetados com as enchentes no Rio Grande do Sul "Digite PIX ou Cartão") '))
                        if pagamento.upper() == "PIX":
                            print("PIX(CNPJ): 92.958.800/0001-38")
                            time.sleep(2)
                            print("Pagamento confirmado! Obrigado por manter nosso planeta mais limpo!")
                        elif pagamento.upper() == "CARTÃO" or pagamento.upper() == "CARTAO":
                            print("Processando pagamento...")
                            time.sleep(2)
                            print("Pagamento confirmado!")
                else:
                    print("Nenhum cliente está cadastrado.")
            case 5: #finalza o programa
                print("Obrigado por usar o nosso programa de cadastro!")
                break

main()
