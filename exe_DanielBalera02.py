"""
Faça um programa que o usuario insira 10 produtos numa tupla. 
Exiba todos os produtos, solicite ao usuário para digitar um nome de produto e exiba a posição dele, em seguida peça para digitar numero entre 0 e 9 e exiba o produto da tupla.
"""

produtos = ()
adicionar_produtos = list(produtos)
for i in range(10):
    produto = input('Insira o nome do produto: ')
    adicionar_produtos.append(produto)
    produtos = tuple(adicionar_produtos)

print(produtos)
nome = input('Insira um nome de um produto: ')

if nome in produtos:
    for i in range(len(produtos)):
        if produtos[i] == nome:
            print(i)
else: 
    print('Esse produto não foi inserido.')

numero = int(input('Insira um numero entre 0 e 9: '))
print(produtos[numero])