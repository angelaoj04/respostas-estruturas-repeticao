populacaoA = 80000
txA = 0.03
populacaoB = 200000
txB = 0.015
anos = 0

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
