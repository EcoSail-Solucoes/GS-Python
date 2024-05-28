**Nomes: Felipe Men dos Santos RM: 557571; Matheus Alcantara Estevão: RM: 558193; Otávio Ferrão: RM 556452**

# Sistema de Cadstro para Viagens

## Objetivo do Projeto:

Criamos um projeto com o objetivo de cadastrar pessoas em um sistema para realizar viagens para 6 diferentes lugares: Santos, Fernando de Noronha, Rio de Janeiro, Recife, Maceió e Miami Beach.

## Funcionamento do Código

O programa inicia criando as váriaveis de listas utilizadas no programa.
Logo após ele cumprimenta o cliente com "Seja Bem-Vindo(a)" e da uma delay de 1 segundo para continuar o código.

![image](https://github.com/EcoSail-Solucoes/GS-Python/assets/153327403/8a788efd-28f0-4b7f-9b9a-e0f34a434481)

Depois ele cria uma função usada para cadastrar um cliente novo, digitado pelo usuário.

![image](https://github.com/EcoSail-Solucoes/GS-Python/assets/153327403/89648b23-4b94-4124-8f37-5d7de0a593b5)

Após criar a função de cadastrar o cliente, ele cria a função main() que é usada para listar as opções do cliente: Cadastrar Cliente, Verificar Clientes, Remover Clientes, Registrar Viagens e Sair.

![image](https://github.com/EcoSail-Solucoes/GS-Python/assets/153327403/cea9c8e8-44f3-4ac1-abd0-b2d0071f10c6)

Utilizando uma variável para guardar a opção do cliente, o programa começa a verificar as opções para realizar o pedido do cliente.

![image](https://github.com/EcoSail-Solucoes/GS-Python/assets/153327403/65d2484f-032e-426c-b481-3279d0fb988b)

Implementando a função do match case o programa le a variavél das opçôes e continua o código.

![image](https://github.com/EcoSail-Solucoes/GS-Python/assets/153327403/91425e5e-0cf3-46b9-a830-d0309f9e49e5)

Se o usuário escolher a opção de cadastrar um cliente, o programa roda a função **get_cadastro()** e adiciona a reposta do usuário na lista **"cadastros"**.

Se o usuário escolher a opção de verificar os clientes, o programa vai verificar se a lista **cadastros** está vazia, se estiver vazia ele mostra uma mensagem avisando que a lista está vazia, se não ele lista o nome de todos os clientes na lista.

Se o usuário escolher a opção de remover um cliente, o programa pede para o usuário digitar o nome de um cliente na lista **cadastros** e remove o mesmo e mostra uma mesagem dizendo que o cliente foi removido com sucesso.

Se o usuário escolher a opção das viagens, o programa cria outro match case com as opções das viagens que estão na lista **viagens** e pergunta qual viagem o usuário deseja fazer.
  Ao escolher sua viagem o programa exibe o nome e preço da viagem selecionada, além de exibir o nome dos clientes que foram registrados na lista **cadastros**.
  E no por final, o programa pergunta ao usuário se o mesmo deseja pagar com PIX, se o usuário digitar "Sim" o programa exibe o PIX para realizar o pagamento, se não o programa exibe uma mensagem dizendo que o pagamento foi cancelado, e logo em seguida finaliza o programa.
  
Se o usuário escolher a opção de sair, o programa mostra uma mensagem agradecendo o usuário por utilizar nosso programa e logo em seguida finaliza o mesmo.


