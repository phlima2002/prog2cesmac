from usuarios.cadastroUsuario import *
from usuarios.autenticacao import *
from produtos.cadastroProduto import *


usuario = cadastrar_usuario()


tentativaEmail, tentativaSenha = login()

if tentativaEmail == usuario['email'] and tentativaSenha == usuario['senha']:
    print('Login bem sucedido')
    produto = cadastrar_produto()
    print(produto)

else:
    print('Login negado.')




