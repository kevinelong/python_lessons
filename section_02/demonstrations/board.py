# Generate Output Grid

# . . .
# . . .
# . . .

# Simple Script

for x in range(0, 3):
    for y in range(0, 3):
        print( ".",)
    print("")


# Generate Output Grid or Any Size

# . . . .
# . . . .
# . . . .
# . . . .

# define the function
def grid(size):
    for x in range(0, size):
        for y in range(0, size):
            print( ".",)
        print("")


# call the function
grid(4)

board = [
    [".", ".", "."],
    [".", ".", "."],
    [".", ".", "."],
]

print(board)


def build_board(size):
    all_rows = []
    for x in range(0, size):
        one_row = []
        for y in range(0, size):
            one_row.append(".")
        all_rows.append(one_row)
    return all_rows


my_board = build_board(12)
print(my_board)


def get_board_string(board):
    output = ""
    for r in board:
        for c in r:
            output = output + " " + c
        output = output + "\n"
    return output


print( get_board_string(my_board))

my_board[6][6] = "X"
print( get_board_string(my_board))

my_board[3][5] = "O"
print( get_board_string(my_board))
