valor = int(input("Insira o valor do produto: "))
imposto = 1.1
valorTotal = valor * imposto

if (valorTotal >= 100):
    print("O produto está caro!")
else:
    print("O produto está em um preço bom!")