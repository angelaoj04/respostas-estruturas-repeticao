soma = 0
media = 0
contador = 1

while (contador <= 5):
    numero = int(input("Informe o número: "))
    soma = soma + numero;
    contador = contador + 1

media = soma / contador
print("A soma dos valores e: ", soma)
print("A média dos valores e: ", media)