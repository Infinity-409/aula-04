"""
Atividade 10:
Crie um programa que peça uma nota entre
0 e 10.
Se o valor for diferente, informe que é
inválido e peça novamente o número até
que o usuário acerte"""

while True:
    nota_valida = float(input('Digite uma nota entre 0 e 10: '))
    if nota_valida >= 0 and nota_valida <= 10:
        print(f'Você digitou uma nota válida, a nota foi: {nota_valida}')
        break
    else:
        print("Nota inválida! Tente novamente com uma nota entre 0 e 10!")
        continue
