produtosCadastrados = []
def cadastrarProduto(): 
    nomeProduto = input('Insira o nome do produto que você deseja cadastrar\n')

    try:
        qtdProduto = int(input('Insira quantas unidades você deseja comprar\n'))
        if(qtdProduto > 0):
            produto = {
            'nome' : nomeProduto.title(),
            'qtd' : qtdProduto
            }
            produtosCadastrados.append(produto)

            print('Produto cadastrado com sucesso')
        else: print('Insira uma quantidade maior que 0')
    except:
        print('Quantidade inválida. Por favor, insira um número inteiro.')


   



    


