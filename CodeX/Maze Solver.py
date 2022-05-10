
from numpy import *

solvable_maze = [
    ["S", "#", "-", "-", "-"],
    ["-", "#", "-", "#", "-"],
    ["-", "#", "-", "#", "-"],
    ["-", "#", "-", "#", "-"],
    ["-", "-", "-", "#", "-"],
    ["#", "-", "-", "#", "X"]
    ]

unsolvable_maze = [
    ["S", "#", "-", "-", "-"],
    ["-", "#", "-", "#", "-"],
    ["-", "#", "-", "#", "-"],
    ["-", "#", "-", "-", "#"],
    ["-", "-", "-", "#", "-"],
    ["#", "-", "-", "#", "X"]
    ]


def solver(maze1):
    maze = maze1.copy()
    for i in maze:
        if "S" in i: a, b = maze.index(i), i.index("S")
    maze[a][b] = "p#"
    while True:
        s = 0
        for a,i in enumerate(maze):
            for b,k in enumerate(i):
                if "p" in k:
                    if "X" in k: return True
                    maze[a][b] = k.replace("p","",1)
                    for h in [(a+1,b),(a-1,b),(a,b+1),(a,b-1)]:
                        try: maze[h[0]][h[1]] += "p#" if h[0] >= 0 and h[1] >= 0 and "#" not in maze[h[0]][h[1]] else ""
                        except: pass
                else: s += 1
        if s == len(maze)*len(i): return False

'''
def solver(maze1):
    maze = maze1.copy()
    for i in maze:
        if "S" in i: a, b = maze.index(i), i.index("S")
    maze[a][b] = "p#"
    while True:
        s = 0
        for a,i in enumerate(maze):
            for b,k in enumerate(i):
                if "p" in k:
                    if "X" in k: return True
                    maze[a][b] = k.replace("p","",1)
                    for h in [(a+1,b),(a-1,b),(a,b+1),(a,b-1)]: exec('try: maze[h[0]][h[1]] += "p#" if h[0] >= 0 and h[1] >= 0 and "#" not in maze[h[0]][h[1]] else ""\nexcept: pass')
                else: s += 1
        if s == len(maze)*len(i): return False
''' 
                            

print(solver(unsolvable_maze))
