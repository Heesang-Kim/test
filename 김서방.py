'''
def solution1(seoul):
    x=["kim"]
    d=-1
    for x in seoul:
        d+=1
        if x:
            break
    answer = "김서방은 %d 에 있다" % d
    return answer
'''
def solution(seoul):
    idx = seoul.index("Kim")
    return idx

print(solution(["Jane", "Kim"]))