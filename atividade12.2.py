"""
Atividade 12.2:
Peça vários números até o usuário decidir
parar. Depois, informe a soma e a média
deles."""

contador = 0
soma = 0


while True:
    numero = float(input(f"Informe o {contador+1}° número: "))
    soma = soma + numero
    pergunta = int(input("Deseja continuar a adicionar números?\n[1] - SIM\n[2] - NÃO\n"))
    contador += 1 
    if pergunta == 1:       
        continue
    else:
        break

media = soma / contador

print(f"A soma dos números é {soma}.")
print(f"A média entre eles é {media}.")