# strings de múltiplas linhas

nome = 'Juliana'

mensagem = f'''
Olá meu nome é {nome}.
Eu estou aprendendo Python.
'''

print(mensagem)
print(mensagem.strip())  # sem os espaços no início e final

# criação de um menu
menu = f'''
    =========== MENU ===========

    [1] Depositar
    [2] Sacar
    [0] Sair

    =============================

    Obrigado por usar nosso app!
'''

print(menu)