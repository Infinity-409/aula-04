"""
Desafio 01:
Crie um programa que leia 5
números e informe o maior
número."""

contador = 1
maior_numero = 0

while contador <= 5:
    numero = float(input(f'Digite o {contador}° número: '))
    if numero > maior_numero:
        maior_numero = numero
    contador += 1

print(f'O maior número digitado foi: {maior_numero}')