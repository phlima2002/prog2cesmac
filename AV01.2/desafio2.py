numeros = [1, 5, 7, 8, 28, 22, 25]
maior = 1
menor = 100
for item in numeros:
    if item > maior:
        maior = item
    if item < menor:
        menor = item

print(f'O menor valor foi {menor}, o maior valor foi {maior} e a soma deles deu {menor + maior}')