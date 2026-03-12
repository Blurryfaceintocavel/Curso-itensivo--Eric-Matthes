#range

n= list (range (1,11))
print (n)

#range com for

for num in range (1,6):
    print(num)

#ignorando alguns números em um dado intervalo.

n1=list (range (2,11,2))
print (n1)

'''OUTROS EXEMPLOS.. '''

quadradros=[]
for valor in range (1,11):
    quadradro= valor **2
    quadradros.append(quadradro)
print (quadradros)

'''squares = [value**2 for value in range(1,11)]
print(squares)'''

print('------------------'  )

'''4.3 – Contando até vinte: Use um laço for para exibir os números de 1 a 20,
incluindo-os.'''

for  vint in range (1,21):
    print(vint)
    
print('-----------------\n-'  )
    
'''4.4 – Um milhão: Crie uma lista de números de um a um milhão e, então, use um
laço for para exibir os números. (Se a saída estiver demorando demais, interrompa
pressionando CTRL-C ou feche a janela de saída.)'''

#for miao in range (1,10000001):
    #print(miao)
    
'''4.5 – Somando um milhão: Crie uma lista de números de um a um milhão e, em
seguida, use min() e max() para garantir que sua lista realmente começa em um e
termina em um milhão. Além disso, utilize a função sum() para ver a rapidez com
que Python é capaz de somar um milhão de números.'''

milao= list (range (1,11)) #tive que trocar pra 10 pq travaria
print ("O numero minimo é:", min (milao))
print ("O numero maximo é:", max (milao))
print ("a soma deles é:", sum (milao))

print('-----------------\n-'  )

'''4.6 – Números ímpares: Use o terceiro argumento da função range() para criar
uma lista de números ímpares de 1 a 20. Utilize um laço for para exibir todos os
números.'''

impares=list (range (1,21,2))
for impar in impares:
    print (f"Numeros impares:", impar)
    
    '''4.7– Três: Crie uma lista de múltiplos de 3, de 3 a 30. Use um laço for para
exibir os números de sua lista.'''


print('-----------------\n-'  )


tres= list (range (3,31,3))

for tre in tres:
    print (f"Multiplos de 3:", tre)
    
print('-----------------\n-'  )
    
cubos= []
for valor in range (1,11):
    cubo= valor **3
    cubos.append(cubo)
print (cubos)

'''4.9 – Comprehension de cubos: Use uma list comprehension para gerar uma lista
dos dez primeiros cubos.'''

cubos= [valor **3 for valor in range (1,11)]
print (cubos)
