def solution(n, lost, reserve):
    answer = 0
    aliver=0
    student=0
    a=0
    b=0
    loststudent=[]
    E=set(reserve)
    while student<n-1:
        while a<n-1:
            if (b in lost) and (b in reserve):
                lost.remove(b)
                reserve.remove(b)
                b-=1
            b+=1
            a+=1
        for loststudent in lost:
            reserve.append((loststudent+1))
            E=set(reserve)
            if len(reserve) != len(list(E)):
                aliver+=1
                reserve.remove(loststudent+1)
            reserve.remove(loststudent+1)
            E=set(reserve)
            if len(reserve) != len(list(E)):
                aliver+=1
                reserve.remove(loststudent-1)
            loststudent=0
            student+=1
    answer=n-len(lost)+aliver
    if answer>n:
        answer=n
    return answer
n=5
lost=[2,4]
reserve=[1,3,5]

solution(n, lost, reserve)