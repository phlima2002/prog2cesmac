# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
turno = input('Digite seu turno: M-matutino V-vespertino ou N-noturno\n')

if turno.lower() == 'm':
    print('Bom dia!')

elif turno.lower() == 'v':
    print('Boa tarde!')

elif turno.lower() == 'n':
    print('Boa noite!')

# O .lower() serve pra sempre estar o caractere minusculo, ja que se o usuario digitasse maiusculo ficaria diferente e geraria erro.

else:
    print('Valor inválido!')
