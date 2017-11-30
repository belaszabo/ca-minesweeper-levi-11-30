import os

SIZE = 10

def init_map(size):
    return [[{'isMine': False, 'isChecked': False} for _ in range(SIZE)] for _ in range(SIZE)]

def draw(grid):
    for row in grid:
      for field in row:
        print("[ ]" if field['isChecked'] else "[?]", end="")
      print()

def check(grid, row, col):
    grid[row][col]['isChecked'] = True

clear = lambda: os.system('clear')

def get_row_and_col():
    fieldToCheck = input("Which field: ")
    row, col = fieldToCheck.split()
    row, col = int(row) - 1, int(col) - 1
    return row, col

def start_game():
    grid = init_map(SIZE)
    draw(grid)
    while True:
      row, col = get_row_and_col()
      check(grid, row, col)
      clear()
      draw(grid)

start_game()
