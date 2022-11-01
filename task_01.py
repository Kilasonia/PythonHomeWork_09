# Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP


OuijaBoard = {'7': ' ', '8': ' ', '9': ' ',
              '4': ' ', '5': ' ', '6': ' ',
              '1': ' ', '2': ' ', '3': ' '}

board_keys = []

for key in OuijaBoard:
    board_keys.append(key)


def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


def game():

    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(OuijaBoard)
        print("Your move," + turn + ".Where to put the sign?")

        move = input()

        if OuijaBoard[move] == ' ':
            OuijaBoard[move] = turn
            count += 1
        else:
            print("This position has already been taken.\nWhere to put the sign?")
            continue

        if count >= 5:
            if OuijaBoard['7'] == OuijaBoard['8'] == OuijaBoard['9'] != ' ':
                printBoard(OuijaBoard)
                print("\nEnd of the game.\n")
                print(" **** " + turn + " victory. ****")
                break
            elif OuijaBoard['4'] == OuijaBoard['5'] == OuijaBoard['6'] != ' ':
                printBoard(OuijaBoard)
                print("\nEnd of the game.\n")
                print(" **** " + turn + " victory. ****")
                break
            elif OuijaBoard['1'] == OuijaBoard['2'] == OuijaBoard['3'] != ' ':
                printBoard(OuijaBoard)
                print("\nEnd of the game.\n")
                print(" **** " + turn + " victory. ****")
                break
            elif OuijaBoard['1'] == OuijaBoard['4'] == OuijaBoard['7'] != ' ':
                printBoard(OuijaBoard)
                print("\nEnd of the game.\n")
                print(" **** " + turn + " victory. ****")
                break
            elif OuijaBoard['2'] == OuijaBoard['5'] == OuijaBoard['8'] != ' ':
                printBoard(OuijaBoard)
                print("\nEnd of the game.\n")
                print(" **** " + turn + " victory. ****")
                break
            elif OuijaBoard['3'] == OuijaBoard['6'] == OuijaBoard['9'] != ' ':
                printBoard(OuijaBoard)
                print("\nEnd of the game.\n")
                print(" **** " + turn + " victory. ****")
                break
            elif OuijaBoard['7'] == OuijaBoard['5'] == OuijaBoard['3'] != ' ':
                printBoard(OuijaBoard)
                print("\nEnd of the game.\n")
                print(" **** " + turn + " victory. ****")
                break
            elif OuijaBoard['1'] == OuijaBoard['5'] == OuijaBoard['9'] != ' ':
                printBoard(OuijaBoard)
                print("\nEnd of the game.\n")
                print(" **** " + turn + " victory. ****")
                break

        if count == 9:
            print("\nEnd of the game.\n")
            print("Draw!!")

        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    restart = input("Do you want to play again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            OuijaBoard[key] = " "

        game()


if __name__ == "__main__":
    game()
