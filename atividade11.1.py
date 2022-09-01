"""
Atividade 11.1:
Refaça a questão anterior, porém, o número secreto será
gerado pelo módulo RANDOM, e sua função RANDINT.
Lembretes:
É preciso importar a biblioteca random.
O randint precisa de um número de início e o fim.
"""

import random

numeroCorreto = random.randint(0,10)

print("JOGO: DESCUBRA O NÚMERO!\n")
while True:
    palpite = int(input("Digite seu palpite (de 0 à 10): "))
    if palpite < numeroCorreto:
        print("\nNúmero ERRADO! Tente um número maior!\n")
    elif palpite > numeroCorreto:
        print("\número ERRADO! Tente um número menor!\n")
    else:
        print("\nVocê acertou! Parabéns!\n")
        break