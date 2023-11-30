n=int(input())
a=input().split()
x_pos_dict=dict(zip(list("abcdefgh"),[i for i in range(8)]))
def decode(chess_pos):
    b=chess_pos[0]
    num=chess_pos[1]
    x=x_pos_dict[b]
    y=8-int(num)
    return [x,y]
board=[["."]*10 for i in range(10)]
horses_pos=[]
for i in a:
    horses_pos.append(decode(i))
for horse in horses_pos:
    acceses_move=[[1,2],[2,1],[-1,2],[-2,1],[-1,-2],[-2,-1],[1,-2],[2,-1]]
    for dpos in acceses_move:
        dx,dy=dpos
        board[horse[1]+dy][horse[0]+dx]="K"
for i in range(8):
    print(*board[i][0:8],sep="")

    
    
