"""
Este módulo demonstra o uso dos operadores de identidade em Python: `is` e `is not`.
Operadores de identidade (`is` e `is not`):
-------------------------------------------------
- O operador `is` verifica se duas variáveis apontam para o mesmo objeto na memória.
- O operador `is not` verifica se duas variáveis NÃO apontam para o mesmo objeto na memória.
Exemplo:
    print(curso is nome_curso)      # True, pois ambos apontam para o mesmo objeto string.
    print(curso is not nome_curso)  # False, pois ambos apontam para o mesmo objeto.
    print(saldo is limite)          # True, pois inteiros pequenos são otimizados e compartilham referência.
Nota:
    Diferente do operador de igualdade (`==`), que compara valores, o operador de identidade compara referências de objetos.
"""

curso = 'Curso de Python'
nome_curso = curso
saldo, limite = 200, 200

print(curso is nome_curso)      # True
print(curso is not nome_curso)  # False
print(saldo is limite)          # True

