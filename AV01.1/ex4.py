# maior de 3 numeros
numero1 = int(input('Digite o primeiro numero\n'))
numero2 = int(input('Digite o segundo numero\n'))
numero3 = int(input('Digite o terceiro numero\n'))

if numero1 > numero2 and numero1 > numero3:
    print(numero1)

if numero2 > numero1 and numero2 > numero3:
    print(numero2)

if numero3 > numero1 and numero3 > numero2:
    print(numero3)
