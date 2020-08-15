def solution(answers):
    answer = []
    a=[]
    b=[]
    c=[]
    d=0
    e=0
    scorea=0
    scoreb=0
    scorec=0
    while d<2000:
        d+=1
        a.append(1)
        a.append(2)
        a.append(3)
        a.append(4)
        a.append(5)
    d=0
    while d<1250:
        d+=1
        b.append(2)
        b.append(1)
        b.append(2)
        b.append(3)
        b.append(2)
        b.append(4)
        b.append(2)
        b.append(5)
    d=0
    while d<1000:
        d+=1
        c.append(3)
        c.append(3)
        c.append(1)
        c.append(1)
        c.append(2)
        c.append(2)
        c.append(4)
        c.append(4)
        c.append(5)
        c.append(5)
    for v in answers:
        if a[e] == v:
            scorea+=1
        e+=1
    e=0
    for v in answers:
        if b[e] == v:
            scoreb+=1
        e+=1
    e=0
    for v in answers:
        if c[e] == v:
            scorec+=1
        e+=1
    if scorea>scoreb and scorea>scorec:
        answer.append(1)
    elif scoreb>scorea and scoreb>scorec:
        answer.append(2)
    elif scorec>scorea and scorec>scoreb:
        answer.append(3)
    elif scorea == scoreb>scorec:
        answer.append(1)
        answer.append(2)
    elif scorea == scorec>scoreb:
        answer.append(1)
        answer.append(3)
    elif scorec == scoreb>scorea:
        answer.append(2)
        answer.append(3)
    else:
        answer.append(1)
        answer.append(2)
        answer.append(3)
    return answer
answers=[1,2,3,4,5]
solution(answers)