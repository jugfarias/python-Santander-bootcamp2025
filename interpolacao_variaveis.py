nome = "Maria"
idade = 30
saldo = 1234.56

# 1. Interpolação usando o operador %
print("Olá, %s! Você tem %d anos e seu saldo é R$ %.2f." % (nome, idade, saldo))    # NÃO RECOMENDADO!!!!

# 2. Interpolação usando o método format
print("Olá, {}! Você tem {} anos e seu saldo é R$ {:.2f}.".format(nome, idade, saldo))
print("Olá, {2}! Você tem {0} anos e seu saldo é R$ {1:.2f}.".format(idade, saldo, nome))
print("Olá, {nome}! Você tem {idade} anos e seu saldo é R$ {saldo:.2f}.".format(nome=nome, idade=idade, saldo=saldo))

# criação do dicionário pessoa
pessoa = {
    "nome": "Maria",
    "idade": 30,
    "saldo": 1234.56
}
print("Olá, {nome}! Você tem {idade} anos e seu saldo é R$ {saldo:.2f}.".format(**pessoa))  # uso de dicionário

# 3. Interpolação usando f-strings (Python 3.6+)
print(f"Olá, {nome}! Você tem {idade} anos e seu saldo é R$ {saldo:.2f}.")  # MAIS RECOMENDADO!!!

PI = 3.14159
print(f'Valor de PI: {PI:.2f}')
print(f'Valor de PI: {PI:10.2f}')