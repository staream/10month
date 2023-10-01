"""
a= input()
a= int(a)
for i in range(1,10):
    print(f"{a} * {i} = {a*i}")
"""
"""
num= input()
num= int(num)
for i in range(num):
    a= input()
    a,b = a.split(" ")
    a=int(a)
    b= int(b)
    print(a+b)
"""
"""
num= input()
num = int(num)
total=0
for i in range(num):
    i1=1+i
    total+= i1
print(total)


total_cost= int(input())
total_var= int(input())
total_cost1=0
for i in range(total_var):
    a= input()
    cost,num= a.split()
    cost,num= int(cost),int(num)
    total_cost1+=cost*num
if total_cost ==total_cost1:
    print("Yes")
else:
    print("No")
"""
""" float는 range에 넣을 수는 없다.
a= input()
a= int(a)
a=int(a/4)
j=""
for i in range(a):
    j+="long "
j+= "int"
print(j)
"""
""" 바로 할 수 있게 하는 것이 sys 라는 것을 import해야 한다.
그리고 int로 변환을 필수
import sys
c= input()
c= int(c)
for i in range(c):
    a,b= sys.stdin.readline().split()
    a= int(a)
    b=int(b)
    print(a+b)
"""
"""
a = input()
a= int(a)
for i in range(a):
    b= input()
    c,d = b.split(" ")
    c=int(c)
    d= int(d)
    print(f"Case #{i+1}: {c+d}")
"""
"""
a= input()
a= int(a)
for i in range(a):
    b= input()
    c,d = b.split(" ")
    c=int(c)
    d= int(d)
    print(f"Case #{i+1}: {c} + {d} = {c+d}")
"""
"""
a= input()
a= int(a)
c="*"
d=" "
for i in range(a):
    print(d*(a-i-1)+c*(i+1))
# 입력에 일정한 트리거가 있을 때 while을 생각했다ㅣ.
while True:
    a= input()
    b,c= a.split(" ")
    b= int(b)
    c=int(c)
    if b==0 and c==0:
        break
    else:
        print(b+c)
"""

a= list(input().split("\n"))
for i in a:
    b,c= i.split(" ")
    b=int(b)
    c=int(c)
    print(b+c)

while True:
    try:
        a,b =map(int, input().split(" "))
        print(a+b)
    except:
        break
# 순서를 모를때 
# 갑자기 이상한 것이 나올 때의 대처로는 try, except를 사용한다.