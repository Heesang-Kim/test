'''
def solution(s):
    answer = s.isdigit()
    if len(list(s)) != 4 or 6:
        answer = False
    else:
        pass
    return answer
s="1,2,3,4"
solution(s)'''
def solution(s):

    return True if len(s) == 4 and s.isdigit() else False
