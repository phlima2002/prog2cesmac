from utils.cadastrarProduto import cadastrarProduto
from utils.excluirProduto import excluirProduto
from utils.cadastrarProduto import produtosCadastrados
from utils.editarProduto import editarProduto


codigo = 0

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