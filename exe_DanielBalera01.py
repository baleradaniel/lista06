"""
Crie uma tupla contendo os nomes de cinco países e exiba toda a tupla. 
Peça ao usuário para inserir um dos países que foram mostrados a ele e, em seguida, exibir o número de índice (ou seja, posição na lista) desse item na tupla.
"""

paises =  ('Brasil','Japão','Noruega','Coreia do Sul','Canadá')
print(paises)

pergunta = input('Insira um dos paises mostrados acima: ')
if pergunta in paises:
    for i in range(len(paises)):
        if paises[i] == pergunta:
            print(i)
else: 
    print('Esse país não está na tupla.')