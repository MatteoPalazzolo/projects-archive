import requests, path

DIR = {
  'L': {'L': 'Left'},
  'R': {'R': 'Right'},
  'U': {'U': 'Up'},
  'D': {'D': 'Down'},
}

s = requests.Session()
r = s.get('http://130.192.5.212:8421/')

text_maze = r.text.replace('<br>','\n').replace('<pre>','').replace('</pre>','')
matrix1_maze = text_maze.split('\n')[1:-1]
matrix2_maze = [list(m) for m in matrix1_maze]

for i, v in enumerate(matrix2_maze):
  for j in range(len(v)):
    if matrix2_maze[i][j] == ' ' or matrix2_maze[i][j] == 'x':
      matrix2_maze[i][j] = 1
    else:
      matrix2_maze[i][j] = 0
    print(matrix2_maze[i][j], end='')
  print('')
  
path_nodes = path.solve_maze(matrix2_maze, (0, 1), (80, 39))
path_dir = [path.path_to_dir(path_nodes, i) for i in range(len(path_nodes)-1)]

for d in path_dir:
  #os.system('cls')
  r1 = s.post('http://130.192.5.212:8421/', data=DIR[d])
  print(r1.text.replace('<br>','\n').replace('<pre>','').replace('</pre>',''))