def solution(board, moves):
    answer = 0
    b=0
    c=[]
    e=0
    d=0
    f=0
    for a in moves:
        while board[b][a-1]==0:
            b=b+1
            if b>=len (board):
                b=0
                break
                f+=1
        c.append(board[b][a-1])
        board[b][a-1]=0
        b=0
        if f==1:
            c.remove(0)
    d=len(c)
    while e<d:
        if c[e]==c[e+1]:
            del c[e]
            del c[e]
            answer+=2
            d-=3
            e=0
        else:
            e+=1
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
solution(board, moves)