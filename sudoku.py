board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]
#definiton des Aufbaus des Spiels, anhand räumlicher Trennung
def print_board(bo):

    for i in range(len(bo)):
        if i % 3 == 0 and i !=0:    # festlegung der trennung der felder durch '-' reihe
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):    # festlegung der trennung durch '|' spalte
            if j % 3 == 0 and j != 0:
                print ("  |  ", end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

#print_board(board)


def solve(bo):
    print(bo)           #Um zu sehen wie das Programm vorgeht um das Sudoku zu lösen.
    find = find_empty(bo)
    if not find:
        return True
    else:
        row,col = find

    for i in range(1,10):           #gehen durch die Zahlen 1-9, prüfen ob diese zahlen 'valide' sind sprich ob wir sie hinzufügen können
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):       # mit der if-schleife versuchen wir das komplette Sudoku-Board zu lösen in dem es nach einer validen Eingabe immer weiter versucht
                return True

            bo[row][col] = 0

    return False            # der Fall false tritt ein wenn der Code durch alle Zahlen geht und keine Lösung findet, d.h. das vorherige eingesetzte Element ist fehlerhaft und muss wieder auf 0 gesetzt werden


#wir müssen prüfen ob unser Board überhaupt benutzbar ist
def valid(bo, num, pos):

    # Reihe Prüfen
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Prüfen der Spalte
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False


        # in welcher der 9 Boxen befinden wir uns

        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y*3, box_y*3 +3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if bo[i][j] == num and (i,j) !=pos:
                    return False
        return True
# Schreiben unsere erste Funktion die die leeren Stellen ausfindig machen soll

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None


print_board(board)
solve(board)
print("//////////////////////")
print_board(board)