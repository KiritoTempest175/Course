def display_board(board):
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   {}   |   {}   |   {}   |".format(board[0][0], board[0][1], board[0][2]))
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   {}   |   {}   |   {}   |".format(board[1][0], board[1][1], board[1][2]))
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   {}   |   {}   |   {}   |".format(board[2][0], board[2][1], board[2][2]))
    print("|       |       |       |")
    print("+-------+-------+-------+")


def enter_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))

            if move < 1 or move > 9:
                print("Please enter a number from 1 to 9.")
                continue

            row = (move - 1) // 3
            col = (move - 1) % 3

            if board[row][col] not in ["X", "O"]:
                board[row][col] = "X"
                break
            else:
                print("That square is already occupied.")

        except ValueError:
            print("Please enter a valid number.")


def make_list_of_free_fields(board):
    free_fields = []

    for row in range(3):
        for col in range(3):
            if board[row][col] not in ["X", "O"]:
                free_fields.append((row, col))

    return free_fields


def victory_for(board, sign):
    for row in range(3):
        if board[row][0] == sign and \
           board[row][1] == sign and \
           board[row][2] == sign:
            return True

    for col in range(3):
        if board[0][col] == sign and \
           board[1][col] == sign and \
           board[2][col] == sign:
            return True

    if board[0][0] == sign and \
       board[1][1] == sign and \
       board[2][2] == sign:
        return True

    if board[0][2] == sign and \
       board[1][1] == sign and \
       board[2][0] == sign:
        return True

    return False


def draw_move(board):

    free_fields = make_list_of_free_fields(board)

    if free_fields:
        row, col = free_fields[0]
        board[row][col] = "O"


board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

display_board(board)

while True:

    enter_move(board)
    display_board(board)

    if victory_for(board, "X"):
        print("You won!")
        break

    if not make_list_of_free_fields(board):
        print("It's a draw!")
        break

    print("Computer's move:")
    draw_move(board)
    display_board(board)

    if victory_for(board, "O"):
        print("Computer won!")
        break

    if not make_list_of_free_fields(board):
        print("It's a draw!")
        break