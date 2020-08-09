populacaoA = int(input("Informe a quantidade de habitantes da população A: "))
txA = float(input("Informe a taxa de crescimento anual da população A: "))

populacaoB = int(input("Informe a quantidade de habitantes da população B: "))
txB = float(input("Informe a taxa de crescimento anual da população B: "))
anos = 0

while(populacaoA <= 0 and populacaoB <= 0 and txA <= 0 and txB <= 0):
    print("Entradas inválidas. Informe novamente os valores.")

    populacaoA = int(input("Informe a quantidade de habitantes da população A: "))
    txA = float(input("Informe a taxa de crescimento anual da população A: "))

    populacaoB = int(input("Informe a quantidade de habitantes da população B: "))
    txB = float(input("Informe a taxa de crescimento anual da população B: "))

while (populacaoA <= populacaoB):
    populacaoA = (populacaoA * txA) + populacaoA
    populacaoB = (populacaoB * txB) + populacaoB
    anos = anos + 1
    if(populacaoA >= populacaoB):
        print("A população A levou ",anos, " anos para alcançar ou ultrapassar a população B.")
        print("População A: ",int(populacaoA))
        print("População B: ", int(populacaoB))
        print("\n")
    else:
        print("Ainda não alcançou!!")
        print("População A: ",int(populacaoA))
        print("População B: ", int(populacaoB))
        print("\n")
