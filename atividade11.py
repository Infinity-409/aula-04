"""
Escolha um número entre 1 e 10 e peça para que o usuário
tente
acertar este valor.
Informe se o palpite é maior ou menor que o número secreto.
Quando o número estiver correto, imprima uma mensagem
para isso."""

numeroCorreto = 3

print("JOGO: DESCUBRA O NÚMERO!")
while True:
    palpite = int(input("Digite seu palpite (de 0 à 10): "))
    if palpite < numeroCorreto:
        print("Número ERRADO! Tente um número maior!")
    elif palpite > numeroCorreto:
        print("Número ERRADO! Tente um número menor!")
    else:
        print("Você acertou! Parabéns!")
        break