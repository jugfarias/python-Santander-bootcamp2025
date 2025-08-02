texto = input('Informe uma frase: ')

VOGAIS = 'aeiou'

# for iterando uma sequência (string, lista, tupla...)
for letra in texto:
    if letra.lower() in VOGAIS:
        print(letra, end=' ')
else: # executa ao final do laço
    print()

'''
for com função range -> iterando um determinado número de vezes:
for {variavel iterada} in range ({valor de parada}, {valor de início - opcional, padrão: 0}, {valor do passo - opcional, padrão: 1})
'''

print('Números entre 1 e 10: ')
for i in range(1, 11):
    print(i, end=' ')
else:
    print()


print('Números pares entre 10 e 49: ')

# for em uma linha criando uma lista
pares = [str(i) for i in range(10, 50, 2)]

print(', '.join(pares))