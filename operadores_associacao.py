"""
Operadores de associação em Python são utilizados para verificar se um valor está presente em uma sequência (como listas, tuplas, strings etc.). 
Os principais operadores de associação são:

- `in`: Retorna True se o valor especificado estiver presente na sequência.
- `not in`: Retorna True se o valor especificado não estiver presente na sequência.

Exemplo:
    valor in lista  # Verifica se 'valor' está na 'lista'
    valor not in lista  # Verifica se 'valor' não está na 'lista'
"""

curso = 'Curso de Python'
frutas = ['laranja', 'uva', 'bergamota']
saques = [1500, 100]

print('Python' in curso)    # True
print('maçã' not in frutas) # True
print(200 in saques)        # False