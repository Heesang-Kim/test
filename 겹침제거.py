def solution(arr):
    llist=[]
    while len(llist)<1000000:
        llist.append(0)
    a=999999
    b=0
    for v in arr:
        if v != llist[a]:
            llist.append(v)
            a+=1
    llist.reverse()
    while b<1000000:
        llist.pop()
        b+=1
    llist.reverse()
    answer=llist
    return answer
arr = [1, 1, 3, 3, 0, 1, 1]
solution(arr)
