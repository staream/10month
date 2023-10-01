"""
a,b,c =input().split(" ")
a= int(a)
b= int(b)
c= int(c)
print((a+b)%c)
print(((a%c)+(b%c))%c)
print((a*b)%c)
print(((a%c)*(b%c))%c)
"""
"""
a= int(input())
b= input()
c= b[1]
d=b[2]
e=b[0]
b=int(b)
c=int(c)
d=int(d)
e=int(e)
print(a*d)
print(a*c)
print(a*e)
print(a*b)
"""
"""
a,b,c=input().split(" ")
a=int(a)
b=int(b)
c=int(c)
print(a+b+c)
"""
print("\\    /\\\n )  ( ')\n(  /  )\n \\(__)|")
print("\\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \\(__)|")

print("|\\_/|\n|q p|   /}\n( 0 )\"\"\"\\\n|\"^\"`    |\n||_/=\\\\__|")
"""
a= input()
b,c = a.split(" ")
b=int(b)
c= int(c)
if b==c:
    print("==")
elif b>c:
    print(">")
elif b<c:
    print("<")
"""
"""
a= input()
a= int(a)
if a>= 90:
    print("A")
elif a>=80:
    print("B")
elif a>=70:
    print("C")
elif a>=60:
    print("D")
else:
    print("F")
"""
"""  윤달 얻기
a= input()
a= int(a)
if a%400==0:
    print(1)
elif a%4==0 and a%100!=0:
    print(1)
else:
    print(0)
    """
"""
x= input()
y= input()
x=int(x)
y= int(y)
if x>0 and y>0:
    print(1)
elif x>0 and y<0:
    print(4)
elif x<0 and y>0:
    print(2)
else:
    print(3)
"""
"""
a= input()
H, M= a.split(" ")
H= int(H)
M= int(M)
if M-45<0:
    if H==0:
        print(23, M+15)
    else:
        print(H-1, M+15)
else:
    print(H, M-45)
    """
""" 오븐 시계 
 분에서 이미 결괏값을 따로 변수처리 했다.
그래서 계속 더해지는 것을 막음
분이 넘는 것과 아닌 것으로 케이스를 나눔.
반복문을 써서 계속 되는 것을 할 수 있게 했고, 일정 기준이 되면 
break을 했다.
a= input()
b=input()
H,M= a.split(" ")
H=int(H)
M=int(M)
b=int(b)
M1=M+b
if M1>=60:
    while True:
        if M1>=60:
            if H==23:
                H=0
                M1=M1-60
            else:
                H=H+1
                M1=M1-60
        elif M1<60:
            M=M1
            break
elif M1<60:
    M=M1  
print(H,M)    
"""

#L=["1","2","4","5",]
#a="-".join(L)


a= input()
a,b,c=a.split(" ")
a= int(a)
b= int(b)
c= int(c)
if a==b and b==c:
    print(10000+a*1000)
elif a==b:
    print(1000 +a*100)
elif b==c:
    print(1000 +b*100)
elif c==a:
    print(1000 +a*100)
else:
    if a>b:
        if c>a:
            print(c*100)
        elif a>c:
            print(a*100)
    elif b>a:
        if b>c:
            print(b*100)
        elif b<c:
            print(c*100)