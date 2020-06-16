

game_state = [
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', '.']
]


def draw():
    for row in game_state:
        line = ''
        for column in row:
            line += column
        print(line)


game_state[1][1] = 'X'
game_state[0][0] = 'O'

draw()
