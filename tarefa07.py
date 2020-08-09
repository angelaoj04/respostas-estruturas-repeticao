maior = -999999999
contador = 1

while (contador <= 5):
    numero = int(input("Informe o número: "))

    if numero > maior:
        maior = numero
    contador = contador + 1

print("O maior número foi: ", maior)
