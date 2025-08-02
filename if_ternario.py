'''
{resultado} if {condição} else {resultado alternativo}
'''

idade = int(input('Qual sua idade? '))
mensagem = "maior de idade" if idade >= 18 else "menor de idade"
print('Você é {}'.format(mensagem))