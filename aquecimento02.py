"""Aquecimento 02:
1) Peça um número inteiro e positivo
2) Peça outro número inteiro e positivo
Construa uma CALCULADORA com as
operações básicas: soma, subtração,
multiplicação e divisão.
Obs: o usuário que irá escolher a operação!"""

numero1 = int(input("Informe o primeiro número: "))
numero2 = int(input("Informe o segundo número: "))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

operacao = int(input("Qual operação vocẽ deseja realizar?\n[1] Adição\n[2] Subtração\n[3] Multiplicação\n[4] Divisão:\n"))

if operacao == 1:
    print(f"A soma entre {numero1} e {numero2} é igual à {soma}.")
elif operacao == 2:
    print(f"A subtração entre {numero1} e {numero2} é igual à {subtracao}.")
elif operacao == 3:
    print(f"A multiplicação entre {numero1} e {numero2} é igual à {multiplicacao}.")
elif operacao == 4:
    print(f"A divisão entre {numero1} e {numero2} é igual à {divisao}.")
else:
    print("Operação é inválida! Rode o código novamente!")
