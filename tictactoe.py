tabuleiro = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
for linha in tabuleiro:                           
        print(" | ".join(linha))

for i in range(9):
    if i % 2 == 0:
        jog = "X"
    else:
        jog = "O"

    jogada = input(f"Jogador {jog}, selecione o local que deseja jogar (1-9): ")                #DECIDE O LUGAR DO TABULEIRO
    while True:
        if jogada == "1" and tabuleiro[0][0] == " ":
            tabuleiro[0][0] = jog
            break
        elif jogada == "2" and tabuleiro[0][1] == " ":
            tabuleiro[0][1] = jog
            break
        elif jogada == "3" and tabuleiro[0][2] == " ":
            tabuleiro[0][2] = jog
            break
        elif jogada == "4" and tabuleiro[1][0] == " ":
            tabuleiro[1][0] = jog
            break
        elif jogada == "5" and tabuleiro[1][1] == " ":
            tabuleiro[1][1] = jog
            break
        elif jogada == "6" and tabuleiro[1][2] == " ":
            tabuleiro[1][2] = jog
            break
        elif jogada == "7" and tabuleiro[2][0] == " ":
            tabuleiro[2][0] = jog
            break
        elif jogada == "8" and tabuleiro[2][1] == " ":
            tabuleiro[2][1] = jog
            break
        elif jogada == "9" and tabuleiro[2][2] == " ":
            tabuleiro[2][2] = jog
            break
        else:
            jogada = input("Jogada inválida, tente novamente: ")

    for linha in tabuleiro:                                    #Tabuleiro
        print(" | ".join(linha))

    if tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] != " ":                     #Vitória
        print(f"Jogador {tabuleiro[0][0]} ganhou!")
        break
    elif tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2] != " ":
        print(f"Jogador {tabuleiro[1][0]} ganhou!")
        break
    elif tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] != " ":
        print(f"Jogador {tabuleiro[2][0]} ganhou!")
        break
    elif tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0] != " ":
        print(f"Jogador {tabuleiro[0][0]} ganhou!")
        break
    elif tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1] != " ":
        print(f"Jogador {tabuleiro[0][1]} ganhou!")
        break
    elif tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2] != " ":
        print(f"Jogador {tabuleiro[0][2]} ganhou!")
        break
    elif tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
        print(f"Jogador {tabuleiro[0][0]} ganhou!")
        break
    elif tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
        print(f"Jogador {tabuleiro[0][2]} ganhou!")
        break