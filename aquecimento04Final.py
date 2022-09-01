"""Aquecimento FINAL:
Crie um código que informe ao usuário se
o número digitado é PAR ou ÍMPAR"""

numero = int(input("Informe um núemro: "))

if (numero % 2 == 0):
    print(f"{numero} é um número PAR!")
else:
    print(f"{numero} é um número ÍMPAR!")