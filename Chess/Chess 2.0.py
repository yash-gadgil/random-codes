from Chessbackendtwo import *

piece_holder = {}
white_playing = False

board = [["0","0","0","0","0","0","0","0"],
         ["0","0","0","0","0","0","0","0"],
         ["0","0","0","0","0","0","0","0"],
         ["0","0","0","0","0","0","0","0"],
         ["0","0","0","0","0","0","0","0"],
         ["0","0","0","0","0","0","0","0"],
         ["0","0","0","0","0","0","0","0"],
         ["0","0","0","0","0","0","0","0"]]

g = [[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12]]

s = CScreen()
t = Drawer()
#s.delay(0)
t.board()
setup(board,white_playing,piece_holder)

print(piece_holder["bpf"].p.moveset(board,white_playing))
#print(get_backward_diagonals(g))
#print(len(turtles()))

#print(type(s))
