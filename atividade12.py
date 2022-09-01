"""
Atividade 12:
Peça 5 números e informe a soma de todos
eles."""

contador = 1
soma = 0

while contador <= 5:
    numero = float(input(f"Informe o {contador}° número: "))
    contador += 1
    soma = soma + numero

print(f"A soma dos números é {soma}.")