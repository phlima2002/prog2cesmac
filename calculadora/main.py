from utils.calculadora import *
from utils.users import create_user

user, criado_em = create_user('Joao', 'Silva')

numero1 = float(input('Digite o primeiro numero: '))
numero2 = float(input('Digite o segundo numero: '))

total = dividir(numero1, numero2)

print(f'Total: {total}')