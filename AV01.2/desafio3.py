array = []
maior = 1
menor = 100

while(len(array) < 10):
    numero = int(input('Digite um numero\n'))
    if numero >= 0 and numero <= 1000:
        array.append(numero)
    else: print('O numero deve estar entre 0 e 1000')

for item in array:
    if item > maior:
        maior = item
    if item < menor:
        menor = item

print(f'O menor valor foi {menor}, o maior valor foi {maior} e a soma deles deu {menor + maior}')