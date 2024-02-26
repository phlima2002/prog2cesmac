#Faça um programa, utilizando while, que permita o usuário fazer contas de adição enquanto quiser.
parametro = 's'
while parametro.lower() != 'n':
    n1 = int(input('Digite um numero\n'))
    n2 = int(input('Digite outro numero\n'))
    print(f'{n1} + {n2} = {n1 + n2}')

    parametro = input('Deseja realizar mais uma soma? (S OU N)\n')
