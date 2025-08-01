# Operadores de identidade (is e is not) são utilizados para comparar se dois objetos têm o mesmo valor

curso = 'Curso de Python'
nome_curso = curso
saldo, limite = 200, 200

print(curso is nome_curso)      # True
print(curso is not nome_curso)  # False
print(saldo is limite)          # True