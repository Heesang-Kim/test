a="life is too short"
print(a[0])
print(a[0:4])
print(a[0:8:2])
number=2
days=7
b="I eat %d rotten food. so i was sick for %d days"%(number, days)
print(b)
print("%-5skim" % "Hi")
print("%0.1f"%3.2345)
print(b.count('s'))
print(b.find('f'))
print(a.index('t'))
c=" but "
print(c.join('abcd'))
print(c.upper())
print(c.strip())
print(a.replace("short", "long"))
print(b.split())
d=[1,2,3,4,5]
print(d[0]+d[4])
d.append(0)#뒤에 추가
print(d)
d.sort()#순서대로
print(d)
d.reverse()#뒤집기
print(d)
print(d.index(3))#4번째것이 뭐야
d.insert(0,9)#0하고 9 삽입해
print(d)
d.remove(0)#0 제거해
print(d)
print(d.pop())
dic={'name':'heesang', 'phonenumber':'010-8731-2778', 'birth':'1204'}
print(dic['birth'])
dic['age']=18
print(dic)
del dic['phonenumber']
print(dic)
print(dic.keys())
print(dic.values())
print(dic.items())
#set():집합. 순서X 중복X
#조건문
pocket=['paper', 'cellphone']
card=True
if 'money' in pocket:
    print("택시를 타고가라")
elif card:
    print("버스를 타고가라")
else:
    print("walk")       
#while문
t=0
while t<10:
    t = t+1
    print("나무를 %d번 찍었습니다"%t)
    if t==10:
        print("나무가 쓰러집니다.")
#for문
score=[90,25,67,45,80]
n=0
for s in score:
    n+=1
    if s >=60:
        print("%d번 학생은 합격입니다."%n)
    else:
        print("%d번 학생은 불합격입니다."%n)
#brake:작동을 멈춘다.
#continue : while, for문의 실행을 생략하고 처음부터 시작한다.
#range(a,b) : (a<=X<b)
#함수
def E(*args):
    sum=0
    for g in args:
        sum += g
    return sum
print(E(1,2,3,4))