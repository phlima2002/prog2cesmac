from utils.cadastrarProduto import cadastrarProduto
from utils.excluirProduto import excluirProduto
from utils.cadastrarProduto import produtosCadastrados
from utils.editarProduto import editarProduto
from utils.cadastrarUsuario import cadastrarUsuario
from utils.autenticarUsuario import autenticarUsuario
codigoAutenticação = 0
codigo = 0

while codigoAutenticação != 3:
   codigoAutenticação = int(input('Digite 1 para cadastrar, 2 para fazer login e 3 pra sair\n'))

   if codigoAutenticação == 1:
      cadastrarUsuario()
   if codigoAutenticação == 2:
      #se a o login for validado, ele entra no menu de cadastro de produtos.
      if autenticarUsuario():
         while codigo != 5:
            codigo = int(input('Digite 1 para cadastrar, 2 para excluir, 3 para editar, 4 para exibir e 5 pra sair\n'))

            if codigo == 1:
               cadastrarProduto()

            if codigo == 2:
               excluirProduto()

            if codigo == 3:
               editarProduto()
            if codigo == 4:
               print(produtosCadastrados)

      else: print('Login invalido!\n')