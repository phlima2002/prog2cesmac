from utils.cadastrarUsuario import usuariosCadastrados

def autenticarUsuario():
    
    email = input('Digite seu email\n')
    senha = input('Digite sua senha\n')

    for usuario in usuariosCadastrados:
        if usuario['email'] == email and usuario['senha'] == senha:
            print('Login realizado com sucesso')
            return True

    print('Email ou senha incorretos')
    return False
