nome = input('Digite um nome\n')
idade = int(input('Digite sua idade\n'))
salario = int(input('Digite seu salário\n'))
sexo = input('Digite seu sexo\n')
estadoCivil = input('Digite seu estado civil\n')

if len(nome) < 4:
    print('O nome deve ter mais que 3 caracteres')

if idade < 0 or idade > 150:
    print('A idade deve ter entre 0 e 150 anos')

if salario < 0:
    print('O salario tem que ser maior que 0')

if sexo.lower() != 'f' or sexo.lower() != 'm':
    print('O sexo tem que ser F ou M')

if estadoCivil.lower() != 's' or estadoCivil.lower() != 'c' or estadoCivil.lower() != 'v' or estadoCivil.lower() != 'd':
    print('O estado civil tem que ser S, C, V ou D')