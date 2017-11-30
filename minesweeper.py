import os
import random

SIZE = 10

def init_map(size):
    return [[{'isMine': False, 'isChecked': False} for _ in range(SIZE)] for _ in range(SIZE)]

def init_mines(grid, max_mines):
    row = random.randint(0, len(grid) - 1)
    col = random.randint(0, len(grid) - 1)
    print(row, col)
    grid[row][col]['isMine'] = True

def draw(grid):
    for row in grid:
      for field in row:
        print('[ ]' if field['isChecked'] else '[?]', end='')
      print()

def check(grid, row, col):
    grid[row][col]['isChecked'] = True
    if grid[row][col]['isMine']:
        return False
    return True

clear = lambda: os.system('clear')

def get_row_and_col():
    fieldToCheck = input('Which field: ')
    row, col = fieldToCheck.split()
    row, col = int(row) - 1, int(col) - 1
    return row, col

def start_game():
    grid = init_map(SIZE)
    init_mines(grid, 10)
    draw(grid)
    is_live = True
    while is_live:
      row, col = get_row_and_col()
      is_live = check(grid, row, col)
      clear()
      draw(grid)

start_game()
