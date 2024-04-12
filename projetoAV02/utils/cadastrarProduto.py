produtosCadastrados = []
def cadastrarProduto(): 

    nomeProduto = input('Insira o nome do produto que você deseja cadastrar\n')
    qtdProduto = int(input('Insira quantas unidades você deseja comprar\n'))

    produto = {
        'nome' : nomeProduto.title(),
        'qtd' : qtdProduto
    }

    produtosCadastrados.append(produto)


    print('Produto cadastrado com sucesso')

    


