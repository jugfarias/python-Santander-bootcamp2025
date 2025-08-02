saldo = 500.0
cheque_especial = 200.0

resp = input('Qual o tipo da sua conta? \n [1] Conta normal\n [2] Conta universitária\nResposta: ')

if resp == '1':
    conta_normal = True
    conta_universitaria = False
elif resp == '2':
    conta_normal = False
    conta_universitaria = True
else: 
    print('Opção invalida!')

if resp == '1' or resp == '2':
    saque = float(input('Quando você deseja sacar? '))
    
    if conta_normal:
        if saldo >= saque:
            print('Saque realizado com sucesso!')
        elif saque <= (saldo + cheque_especial):
            print('Saque realizado utilizando o cheque especial.')
        else:
            print('Saldo insuficiente.')
    elif conta_universitaria:
        if saldo >= saque:
            print('Saque realizado com sucesso.')
        else:
            print('Saldo insuficiente.')


