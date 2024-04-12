from utils.cadastrarProduto import produtosCadastrados

def editarProduto():
    nomeProduto = input('Insira o nome do produto que você deseja editar\n')

    for produto in produtosCadastrados:
        if produto['nome'].lower() == nomeProduto.lower():
            novoNome = input('Insira o novo nome do produto (ou deixe em branco para manter o mesmo)\n')
            novaQtd = input('Insira a nova quantidade do produto (ou deixe em branco para manter a mesma)\n')

            if novoNome:
                produto['nome'] = novoNome.title()
            if novaQtd:
                produto['qtd'] = int(novaQtd)

            print('Produto editado com sucesso')
            return

    print('Produto não encontrado')



