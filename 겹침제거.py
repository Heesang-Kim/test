def solution(arr):
    llist=[0]
    a=0
    b=0
    for v in arr:
        if v != llist[a]:
            llist.append(v)
            a+=1
    llist.reverse()
    llist.pop()
    llist.reverse()
    answer=llist
    return answer
arr = [1, 1, 3, 3, 0, 1, 1]
solution(arr)
