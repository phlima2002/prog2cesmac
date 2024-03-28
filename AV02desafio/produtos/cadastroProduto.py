def cadastrar_produto():
    nomeProduto = input('Digite o nome do produto que deseja cadastrar\n')
    precoProduto = int(input('Digite o preço do produto que deseja cadastrar\n'))

    novo_produto = {
        'nomeProduto': nomeProduto,
        'precoProduto': precoProduto
    }

    return novo_produto