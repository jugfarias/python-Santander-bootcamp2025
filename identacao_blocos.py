def sacar(saldo, valor):
    if saldo >= valor:
        saldo -= valor
        print('valor sacado')
        print('agora você tem {} na conta'.format(saldo)) 
    else:
        print('dinheiro insuficiente')
        print('você tem {} na conta'.format(saldo)) 
    
    print('obrigado por ser nosso cliente, tenha um bom dia!')

    return saldo

def depositar(saldo, valor):
    saldo += valor

    print('agora você tem {} na conta'.format(saldo)) 

    return saldo

saldo = 500

saldo = sacar(saldo, 100)
saldo = sacar(saldo, 1000)

saldo = depositar(saldo, 300)