#Ordenando uma lista de forma permanente com o método sort()

#.8 – Conhecendo o mundo: Pense em pelo menos cinco lugares do mundo que
#você gostaria de visitar.

pais= ['Londres', 'Coreia', 'Canada', 'Grecia', 'Africa', 'Suíça']

print(pais)

print ("============================")

'''Utilize sorted() para exibir sua lista em ordem alfabética, sem modificar a lista
propriamente dita.'''

print (sorted (pais))  #ordem alfa

print ("============================")

'''Utilize sorted() para exibir sua lista em ordem alfabética inversa sem alterar a
ordem da lista original.'''

sort_rev= sorted(pais, reverse=True)

print(sort_rev)
       
print ("============================")

'''Utilize reverse() para mudar a ordem de sua lista. Exiba a lista para mostrar
que sua ordem mudou'''

pais.reverse()
print (pais)

''' Utilize sort() para mudar sua lista de modo que ela seja armazenada em
ordem alfabética. Exiba a lista para mostrar que sua ordem mudou.'''

pais.sort()
print(pais)

pais.sort(reverse=True)
print (pais)

#Convidados para o jantar: Trabalhando com um dos programas dos
#Exercícios de 3.4 a 3.7 (páginas 80 e 81), use len() para exibir uma mensagem
#informando o número de pessoas que você está convidando para o jantar.

convidado= ["Ace", "David", "Kurt"]
num=len (convidado) 
print("Número de convidados para o jantar: " + str(num))

#3.10 – Todas as funções: Pensa em algo que você poderia armazenar em uma
#lista. Por exemplo, você poderia criar uma lista de montanhas, rios, países,
#cidades, idiomas ou qualquer outro item que quiser. Escreva um programa que crie
#uma lista contendo esses itens e então utilize cada função apresentada neste
#capítulo pelo menos uma vez.

idioma= ['Inglês', 'Espanhol', 'Francês', 'Português', 'Italiano']
print(idioma)

idioma.insert (0,'Alemão')

idioma.remove('Francês')

print(sorted(idioma))