# Exemplos de métodos úteis de strings em Python

texto = '  Python bootcamp 2025  '

# strip(): remove espaços em branco do início e do fim
texto_limpo = texto.strip()
print(texto_limpo)  # 'Python bootcamp 2025'

# lstrip(): limpa os espaços em branco do lado esquerdo
print(texto.lstrip())   # 'Python bootcamp 2025  '

# rstrip(): limpa os espaços em branco do lado direito
print(texto.rstrip())   # '  Python bootcamp 2025'

# lower(): converte para minúsculas
print(texto_limpo.lower())  # 'python bootcamp 2025'

# upper(): converte para maiúsculas
print(texto_limpo.upper())  # 'PYTHON BOOTCAMP 2025'

# title(): converte para título (iniciais maiúsculas)
print(texto_limpo.title())

# center(): centraliza o texto envolto de um caractere selecionado - center({nº de caracteres total do texto}, {caractere - opcional})
print(texto_limpo.center(24, '#'))  # '##Python bootcamp 2025##'

# join(): junta os caracteres da string por um caractere selecionado - join({caractere}.join({string/lista}))
print('.'.join('Python'))

# replace(): substitui partes da string
novo_texto = texto_limpo.replace('2025', '2024')
print(novo_texto)  # 'Python bootcamp 2024'

# split(): divide a string em uma lista usando um separador
palavras = texto_limpo.split()
print(palavras)  # ['Python', 'bootcamp', '2025']

# join(): junta elementos de uma lista em uma string
frase = "-".join(palavras)
print(frase)  # 'Python-bootcamp-2025'

# find(): retorna o índice da primeira ocorrência de um substring
indice = texto_limpo.find('bootcamp')
print(indice)  # 7

# startswith() e endswith(): verifica início/fim da string
print(texto_limpo.startswith('Python'))  # True
print(texto_limpo.endswith('2025'))      # True

# count(): conta quantas vezes um substring aparece
print(texto_limpo.count('o'))  # 3

# isdigit(): verifica se a string contém apenas dígitos
ano = '2025'
print(ano.isdigit())  # True