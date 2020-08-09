nome = ""
while len(nome) <= 3:
    nome = input("Informe seu nome: ")
    if len(nome) <= 3:
        print("O nome deve ter mais de 3 letras")
    else:
        print("O nome tem mais de 3 letras")

idade = -1
while(idade <0 or idade > 150):
    idade_str = input("Informe sua idade: ")
    idade = int(idade_str)
    if (idade <0 or idade > 150):
        print("Idade inválida. Informe idade entre acima de 0 e abaixo de 150")
    else:
        print("Idade válida!")

salario = 0
while(salario <= 0):
    salario_str = input("Informe o salário: ")
    salario = float(salario_str)
    if(salario <= 0):
        print("Salário inválido. Informe um salário acima de 0")
    else:
        print("Salário válido!")

sexo = ""
while(sexo.upper() != "M" and sexo.upper() != "F"):
    sexo = input("Informe o sexo: ")
    if(sexo.upper() != "M" and sexo.upper() != "F"):
        print("Sexo inválido! Informe para sexo f ou m")
    else:
        print("Sexo válido!")

estadoCivil = ""
while(estadoCivil.upper() != "S" and estadoCivil.upper() != "C" and estadoCivil.upper() != "D" and estadoCivil.upper() != "V"):
    estadoCivil = input("Informe o estado civil: ")
    if(estadoCivil.upper() != "S" and estadoCivil.upper() != "C" and estadoCivil.upper() != "D" and estadoCivil.upper() != "V"):
        print("Estado civil inválido! Informe para sexo C, D, V ou S")
    else:
        print("Estado civil válido!")