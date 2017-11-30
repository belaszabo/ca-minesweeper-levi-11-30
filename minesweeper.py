SIZE = 10

def init_map(size):
    return [[{'isMine': False, 'isChecked': False} for _ in range(SIZE)] for _ in range(SIZE)]

def draw(grid):
    for row in grid:
      for field in row:
        print("[ ]" if field['isChecked'] else "[?]", end="")
      print()

grid = init_map(SIZE)
