numeros_impares = []

for numero in range(1, 11):
    if numero % 2 == 0:
        continue  # pula os números pares

    numeros_impares.append(str(numero))

print('Números ímpares entre 1 e 10: ', end='')
print(', '.join(numeros_impares))