import time

saldo = 2000.0
saque = float(input('Informe o valor do saque: '))

if saldo >= saque:
    print('Realizando saque...')
    time.sleep(1.5)
    saldo -= saque
    print('R${:.2f} sacado. Agora você tem R${:.2f} na conta.'.format(saque, saldo))
else:
    print('Saldo insuficiente. Você tem R${:.2f} na conta.'.format(saldo))
