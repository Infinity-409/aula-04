"""
Desafio 02:
Encontre uma biblioteca que faça com que o print
ocorra a cada UM SEGUNDO (1s).
A partir disso, crie uma contagem regressiva de 10
até 0 e no final exiba a mensagem:
FELIZ ANO NOVO!"""

import time

contador = 10

while contador >= 0:
    print(contador)
    time.sleep(1)
    contador = contador - 1

print("FELIZ ANO NOVO!!!")