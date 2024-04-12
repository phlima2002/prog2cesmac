from utils.cadastrarProduto import produtosCadastrados

def excluirProduto():
    nomeProduto = input('Insira o nome do produto que você deseja excluir\n')

    for produto in produtosCadastrados:
        if produto['nome'].lower() == nomeProduto.lower():
            produtosCadastrados.remove(produto)
            print('Produto excluído com sucesso')
        else: print('Produto não encontrado')

    
        





    