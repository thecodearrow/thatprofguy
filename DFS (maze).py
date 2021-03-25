


from termcolor import colored #For terminal colors

def printMaze(maze):
  for i in range(5):
    for j in range(5):
      print(maze[i][j],end=" ")
    print()

  print()



def valid(i,j):
  #boundary check
  if(i<0 or j<0 or i>=5 or j>=5):
    return False
  return True

def findPathDFS(i,j,maze,visited):
  if(not valid(i,j)):
    return
  if(visited[i][j]):
    return 
  if(maze[i][j]=='O'):
    return
  if(maze[i][j]=='T'):
    print("YAY!")
    return
  visited[i][j]=True
  maze[i][j]=colored('X','yellow','on_green')
  printMaze(maze)
  findPathDFS(i+1,j,maze,visited) #down
  findPathDFS(i-1,j,maze,visited) #up
  findPathDFS(i,j-1,maze,visited) #left
  findPathDFS(i,j+1,maze,visited) #right

maze=[["." for j in range(5)]for i in range(5)]
maze[0][0]='S'
maze[4][4]='T'
maze[1][0]='O'
maze[1][1]='O'
maze[1][2]='O'
maze[1][3]='O'
maze[3][1]='O'
maze[3][2]='O'
maze[3][3]='O'
maze[3][4]='O'

printMaze(maze)

visited=[[False for j in range(5)] for i in range(5)]
findPathDFS(0,0,maze,visited)




