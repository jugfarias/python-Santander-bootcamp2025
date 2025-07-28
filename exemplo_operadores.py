saldo = 1000.0
saque = 250.0
limite = 200.0
conta_especial = True

condicao1 = saldo >= saque
condicao2 = saque <= limite
condicao3 = conta_especial

if ((condicao1 and condicao2) or (condicao1 and condicao3)):
    print('Você pode sacar {}'.format(saque))