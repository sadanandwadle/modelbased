grid = [
    ['S', '.', '.'],
    ['#', '#', '.'],
    ['.', '.', 'G']
]

position = [0, 0]
visited = []

while True:
    x, y = position

    print("Current position:", position)

    if grid[x][y] == 'G':
        print("Reached goal!")
        break

    visited.append(tuple(position))

    if (y + 1 < 3 and grid[x][y + 1] != '#'
            and (x, y + 1) not in visited):
        position[1] += 1

    elif (x + 1 < 3 and grid[x + 1][y] != '#'
            and (x + 1, y) not in visited):
        position[0] += 1

    elif (y - 1 >= 0 and grid[x][y - 1] != '#'
            and (x, y - 1) not in visited):
        position[1] -= 1

    elif (x - 1 >= 0 and grid[x - 1][y] != '#'
            and (x - 1, y) not in visited):
        position[0] -= 1

    else:
        print("No valid move!")
        break











