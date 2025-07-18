def jogada(play):
    match play:
        case 1 if tabuleiro[0][0] == " ":
            tabuleiro[0][0] = jog
        case 2 if tabuleiro[0][1] == " ":
            tabuleiro[0][1] = jog
        case 3 if tabuleiro[0][2] == " ":
            tabuleiro[0][2] = jog
        case 4 if tabuleiro[1][0] == " ":
            tabuleiro[1][0] = jog
        case 5 if tabuleiro[1][1] == " ":
            tabuleiro[1][1] = jog
        case 6 if tabuleiro[1][2] == " ":
            tabuleiro[1][2] = jog
        case 7 if tabuleiro[2][0] == " ":
            tabuleiro[2][0] = jog
        case 8 if tabuleiro[2][1] == " ":
            tabuleiro[2][1] = jog
        case 9 if tabuleiro[2][2] == " ":
            tabuleiro[2][2] = jog
        case _:
            print("Jogada inválida, tente novamente: ")
            return jogada(int(input()))

tabuleiro = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
win = False

for linha in tabuleiro:                           
        print(" | ".join(linha))

for i in range(9):
    if i % 2 == 0:
        jog = "X"
    else:
        jog = "O"

    jogada(int(input("Onde deseja jogar? (1 - 9) ")))

    for linha in tabuleiro:                                    #Tabuleiro
        print(" | ".join(linha))

    match tabuleiro:
        case tabuleiro if (tabuleiro[0] == ["X"] * 3) or (tabuleiro[0] == ["O"] * 3):                     #Vitória
            print(f"Jogador {tabuleiro[0][0]} ganhou!")
            win = True
        case tabuleiro if (tabuleiro[1] == ["X"] * 3) or (tabuleiro[1] == ["O"] * 3):
            print(f"Jogador {tabuleiro[1][0]} ganhou!")
            win = True
        case tabuleiro if (tabuleiro[2] == ["X"] * 3) or (tabuleiro[2] == ["O"] * 3):
            print(f"Jogador {tabuleiro[2][0]} ganhou!")
            win = True
        case tabuleiro if tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0] != " ":
            print(f"Jogador {tabuleiro[0][0]} ganhou!")
            win = True
        case tabuleiro if tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1] != " ":
            print(f"Jogador {tabuleiro[0][1]} ganhou!")
            win = True
        case tabuleiro if tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2] != " ":
            print(f"Jogador {tabuleiro[0][2]} ganhou!")
            win = True
        case tabuleiro if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
            print(f"Jogador {tabuleiro[0][0]} ganhou!")
            win = True
        case tabuleiro if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
            print(f"Jogador {tabuleiro[0][2]} ganhou!")
            win = True
    if win == True:
        break