usuariosCadastrados = []

def cadastrarUsuario():
    email = input('Insira seu email: ')
    senha = input('Insira sua senha: ')
    
    usuario = {
        'email': email,
        'senha': senha
    }
    
    usuariosCadastrados.append(usuario)
    print('Usuário cadastrado com sucesso')
    print(usuariosCadastrados)