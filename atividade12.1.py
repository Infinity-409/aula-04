"""
Atividade 12.1:
Peça 5 números e informe a soma de todos
eles e a média"""

contador = 0
soma = 0


while contador < 5:
    numero = float(input(f"Informe o {contador+1}° número: "))
    soma = soma + numero
    contador += 1

media = soma / contador

print(f"A soma dos números é {soma}.")
print(f"A média entre eles é {media}.")

