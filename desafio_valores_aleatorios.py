"""  Desafio Random!! 

 Jogue dois itens numa lista "cara " e "coroa" e cria um programa que imprima randomicamente as opções na lista!! """

import random

l1 = ['cara', 'coroa']
print(random.choice(l1))

""" Crie uma lista de 5 nomes, e crie um programa que realize um sorteio entre eles  """

participantes = ["Gabriel ", "João", "Ana ", "Larissa", "Fernando"]
print(random.choice(participantes))

"""Escolha aleatoriamente um número entre 10 e 100"""

print(random.randint(10, 100))