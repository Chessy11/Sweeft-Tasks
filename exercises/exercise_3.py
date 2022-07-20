# Exercise 3: ⬤
# Bomberman lives in a rectangular grid. Each cell in the grid either contains a bomb or
# nothing at all.
# Each bomb can be planted in any cell of the grid but once planted, it will detonate after
# exactly 3 seconds. Once a bomb detonates, it&#39;s destroyed — along with anything in its four
# neighboring cells. This means that if a bomb detonates in cell i, j, any valid cells ( i ± 1, j )
# and ( i, j ± 1 ) are cleared. If there is a bomb in a neighboring cell, the neighboring bomb is
# destroyed without detonating, so there&#39;s no chain reaction.
# Bomberman is immune to bombs, so he can move freely throughout the grid. Here&#39;s what he
# does:
# 1. Initially, Bomberman arbitrarily plants bombs in some of the cells, the initial state.
# 2. After one second, Bomberman does nothing.
# 3. After one more second, Bomberman plants bombs in all cells without bombs,
# thus filling the whole grid with bombs. No bombs detonate at this point.
# 4. After one more second, any bombs planted exactly three seconds ago will
# detonate.
# Here, Bomberman stands back and observes.
# 5. Bomberman then repeats steps 3 and 4 indefinitely.
# Note that during every second Bomberman plants bombs, the bombs are planted
# simultaneously (i.e., at the exact same moment), and any bombs planted at the same time
# will detonate at the same time.
# Given the initial configuration of the grid with the locations of Bomberman&#39;s first batch of
# planted bombs, determine the state of the grid after N seconds.
# For example, if the initial grid looks like:
# . . .
# .O.
# . . .
# It looks the same after the first second. After the second second, Bomberman has placed all
# his charges:
# OOO
# OOO
# OOO
# At the third second, the bomb in the middle blows up, emptying all surrounding cells:
# O.O
# ...

# O.O
# Function Description
# Create the bomber_man function with following parameter(s):
# ● int n: the number of seconds to simulate
# ● string grid[r]: an array of string that represents the grid
# Returns
# ● string[r]: n array of string that represent the grid in its final state





# Sample Input:
# 6 7 3
# . . . . . . .
# . . . O . . .
# . . . . O . .
# . . . . . . .
# OO . . . . .
# OO . . . . .


# Sample Input:
# OOO . OOO
# OO . . . OO
# OOO . . . O
# . . OO . OO
# . . . OOOO
# . . . OOOO



def createGrid(r, c, grid_at_previous_step):
    grid_at_next_step = [['O'] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            current_cell = grid_at_previous_step[i][j]
            if current_cell == 'O':
                grid_at_next_step[i][j] = '.'
                if i - 1 >= 0:
                    grid_at_next_step[i - 1][j] = '.'
                if i + 1 <= r - 1:
                    grid_at_next_step[i + 1][j] = '.'
                if j - 1 >= 0:
                    grid_at_next_step[i][j - 1] = '.'
                if j + 1 <= c - 1:
                    grid_at_next_step[i][j + 1] = '.'
    return grid_at_next_step


def bomberMan(n, r, c, initial_grid):

    grid_after_first_detonation = createGrid(r, c, initial_grid)

    if n % 2 == 0:
        return [['O'] * c for _ in range(r)]
    elif n < 4:
        return initial_grid if n == 1 else grid_after_first_detonation
    else:
        grid_after_second_detonation = createGrid(r, c, grid_after_first_detonation)
        grid_after_third_detonation = createGrid(r, c, grid_after_second_detonation)
        return grid_after_second_detonation if n % 4 == 1 else grid_after_third_detonation

if __name__ == "__main__":
    r, c, n = input().strip().split(' ')
    r, c, n = [int(r), int(c), int(n)]
    grid = []
    for _ in range(r):
       grid.append(list(str(input().strip())))
    result = bomberMan(n, r, c, grid)
    for row in result:
        print("".join(row))
        
        




