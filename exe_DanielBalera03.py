"""
Peça ao usuário para inserir os nomes de três pessoas que deseja convidar para uma festa e armazená-las em uma lista. 
Depois de inserir os três nomes, pergunte se deseja adicionar outro. 
Se o fizer, permita que adicione mais nomes até responder "não". 
Quando ele responder "não", mostre quantas pessoas ele convidou para a festa, uma vez que o usuário tenha completado sua lista de nomes, 
exiba a lista completa e peça que ele digite um dos nomes da lista. 
Exiba a posição desse nome na lista. 
Pergunte ao usuário se ele ainda deseja que essa pessoa venha à festa. Se ele responder "não", exclua essa entrada da lista e exiba a lista novamente.
"""

convidados = []

for i in range(3):
    nome = input('Insira o nome da {}ª pessoa que deseja convidar: '.format(i + 1))
    convidados.append(nome)

confirmacao_usuario = input('Deseja adicionar outro convidado? ("s"/"n") ')

while confirmacao_usuario == 's':
    
    nome = input('Insira o nome da pessoa que deseja convidar: ')
    convidados.append(nome)
    confirmacao_usuario = input('Deseja adicionar outro convidado? ("s"/"n") ')

print('Convidados:\n{}'.format(convidados))
convidado_escolhido = input('Escolha um usuario para exibir sua posição: ')

if convidado_escolhido in convidados:
    for i in range(len(convidados)):
        if convidados[i] == convidado_escolhido:
            
            print('A posição de {} é {}'.format(convidados[i],i))
else:
    print('Este convidado não está na lista.')

confirmacao_convidado = input('Ainda deseja convidar {}? ("sim"/"não")'.format(convidado_escolhido))
if confirmacao_convidado == 'não':
    convidados.remove(convidado_escolhido)

print(convidados)

print('Daniel Balera')