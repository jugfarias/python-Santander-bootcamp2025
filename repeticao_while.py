import time

resp = 0

while resp < 1 or resp > 2:
    resp = float(input('Escolha um número entre 1 e 2: '))

print('Você escolheu o número: {}'.format(resp))

opcao = -1

while opcao != 0:
    opcao = int(input(' [1] Sacar\n [2] Extrato\n [0] Sair\n: '))

    if opcao == 1:
        print('Sacando...')
    elif opcao == 2:
        print('Exibindo extrato...')
    elif opcao == 0:
        print('Saindo...')
    else:
        print('Opção inválida, tente novamente.')
    
    time.sleep(1.5)

else:
    print('Obrigado por utilizar nosso app. Volte sempre!')