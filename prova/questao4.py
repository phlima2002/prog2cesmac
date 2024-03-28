codigo = 0
usuarios = []


while codigo != 3: 
    codigo = int(input('Digite 1 se deseja se cadastrar, 2 se deseja logar, 3 se deseja sair. Apenas criacao de uma conta permitida\n'))
    if codigo == 1:
        usuario = input('Digite um usuario\n')
        senha = input('Digite uma senha\n')
        usuarios.append({
            'username': usuario,
            'password': senha
        })


    if codigo == 2:
        tentativaU = input('Digite seu usuario\n')
        tentativaS = input('Digite sua senha\n')
        for usuario in usuarios:
            print(usuario)
            if usuario['username'] == tentativaU and usuario['password'] == tentativaS:
                # print('Entrou')
                
    


    
    




