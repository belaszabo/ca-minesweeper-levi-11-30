SIZE = 10

grid = init_map(SIZE)

def init_map(size):
    return [[{'isMine': False, 'isChecked': False} for _ in range(SIZE)] for _ in range(SIZE)]
