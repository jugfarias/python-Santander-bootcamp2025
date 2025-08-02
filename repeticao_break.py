# Exemplo de uso do break em um loop

while True:
    resposta = input("Digite 'sair' para encerrar o loop: ")
    if resposta.lower() == 'sair':
        print("Loop encerrado!")
        break
    print("Você digitou:", resposta)