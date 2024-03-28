usuarios = []

def cadastrar_usuario():
    nome = input("Digite seu nome: ")
    telefone = input("Digite seu telefone: ")
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")

    # Criando um dicionário com os dados do usuário
    novo_usuario = {
        'nome': nome,
        'telefone': telefone,
        'email': email,
        'senha': senha
    }

    # Adicionando o novo usuário à lista de dicionários
    usuarios.append(novo_usuario)
    print("Usuário cadastrado com sucesso!")

    return novo_usuario