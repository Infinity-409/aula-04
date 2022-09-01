"""
Atividade 07:
Imprima todos os números pares de 0 à
100.
Logo depois, imprima todos os números
ímpares de 0 à 100."""

contador = 0
print("Números PARES de 0 à 100:")

while contador <= 100:
    if contador % 2 == 0:
        print(contador)
    contador += 1

print("\nNúmeros ÍMPARES de 0 à 100:")

contador = 0
while contador <= 100:
    if contador % 2 == 1:
        print(contador)
    contador += 1

print("\nFIM!")