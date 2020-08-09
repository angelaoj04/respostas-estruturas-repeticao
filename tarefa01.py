nota_str = input("Informe a nota entre 0 e 10: ")
nota = float(nota_str)

while(nota > 10 or nota < 0):
        print("Nota inválida.")
        nota_str = input("Informe uma nota entre 0 e 10: ")
        nota = float(nota_str)
if (nota <=10 or nota >=0):
    print("Nota válida!.")


