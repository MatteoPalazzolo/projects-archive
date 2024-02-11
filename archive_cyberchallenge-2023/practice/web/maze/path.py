from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder


matrix = [
  [1, 1, 1],
  [1, 0, 1],
  [1, 1, 1]
]

def solve_maze(matrix, start, end):

  grid = Grid(matrix=matrix)

  start = grid.node(*start)
  end = grid.node(end[0]-1, end[1]-1)

  finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
  path, runs = finder.find_path(start, end, grid)

  print('operations:', runs, 'path length:', len(path))
  print(grid.grid_str(path=path, start=start, end=end))

  return path


def path_to_dir(path, i):
  try:
    x, y = path[i]
    nx, ny = path[i+1]
    if nx == x+1:
      return 'R'
    elif nx == x-1:
      return 'L'
    elif ny == y+1:
      return 'D'
    elif ny == y-1:
      return 'U'
    else:
      raise Exception('error in path_to_dir')
  except IndexError:
    return