#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
contador = 0
p1 = input('Telefonou para a vitima?\n')
p2 = input('Esteve no local do crime?\n')
p3 = input('Mora perto da vitima?\n')
p4 = input('Devia para a vitima?\n')
p5 = input('Ja trabalhou com a vitima?\n')

if p1.lower() == 'sim':
    contador+= 1

if p2.lower() == 'sim':
    contador+= 1

if p3.lower() == 'sim':
    contador+= 1

if p4.lower() == 'sim':
    contador+= 1

if p5.lower() == 'sim':
    contador+= 1

if contador < 2:
    print('Inocente')

if contador == 2:
    print('Suspeita')

if contador > 2 and contador < 5:
    print('Cumplice')

if contador == 5: 
    print('Assassino')


    

