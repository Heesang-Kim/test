
def solution(participant, completion):
    a=0
    b=0
    c=len(participant)-1
    while b<c:
        participant.remove(completion[a])
        del completion[a]
        b+=1        
    answer = ''.join(participant)
    return answer
    