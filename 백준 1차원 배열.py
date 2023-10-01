"""
# 틀린 것
a= input()
a= int(a)
b= input()
c= input()
e=0
for i in range(2*a-1):
    if b[i]==c:
        e+=1
    else:
        pass
print(e)

#답
a= int(input()) #11
b=list(map(int,input().split(" ")))#1 4 1 2 4 2 4 2 3 4 4
# 빈칸이 있는 숫자열은 strip을 쓸 수 가 없다.
# strip은 앞과 뒤만 가능
c=int(input())#2
print(b.count(c))
"""

#2번
a, b= map(int,input().split())
c=list(map(int,input().split(" ")))
d=""
for i in range(a):
    if c[i]<b:
        print(c[i], end=" ")
"""
        d+=str(c[i])+" "
print(d)
"""

a= int(input())
b= list(map(int,input().split(" ")))
print(min(b),max(b))

# 최댓값 구하기 문제 위가 내가 했던 것
# 문제를 독해를 못했음
l=[]
while True:
    a= int(input())
    if a:
        l.append(a)
    else:
        break
l1= list.index(max(l))
print( max(l), l1)

l=[]
for i in range(9):
    a= int(input())
    l.append(a)
l1= l.index(max(l))# l 대신 list를 계속 넣었다.
print( max(l), l1+1)# index는 0부터 시작한다.

#10810번 공넣기
basket, ball= list(map(int, input().split(" ")))
l=[]
s=""
for i in range(basket):
    l.append(0)

for i in range(ball):
    i_bas,a_bas,bal=map(int,input().split(" "))
    for i in range(i_bas-1,a_bas):
        l[i]=bal
for i in range(basket):
    s+=f"{l[i]} "
print(s)

#10813번 공 바꾸기
a,b = map(int,input().split(" "))
l=[]
s=""
for i in range(a):
    l.append(i+1)
for i in range(b):
    c,d = map(int, input().split(" "))
    l[c-1],l[d-1]=l[d-1],l[c-1]
for i in range(a):
    s+=f"{l[i]} "
print(s)




# << 5597>>
L=[1,2,3,4,5,6,7,8,9]
#for i in L:range(28):
#    i=int(input())
#    L.append(i)
L.sort()
for i in range(10):
    if i<8:
        if L[i]+1==L[i+1]:
            pass
        elif L[i]+1!=L[i+1]:
            print(L[i]+1)
 문제에서 나오지 않았던 이유는 끝에 있는 수가 비어있을 때는 
 찾을 수가 없다는 것이다.
Ex) [1,2,3,4,5,] 6이 최대

#나는 아예 처음부터 다 일일이 세서 보는 방안으로 보았다.
#하지만 답안에선 remove를 사용해서 바로 밥상을 만드는 장면이다.\
# 두번째 range에선 31까지 해서 in을 사용한 경우도 많다.

답
L=[]#[1,2,3,4,5,6,7,8,9]
S=[]
for i in range(28):
    i=int(input())
    L.append(i)
L.sort()
for i in range(1,31):# 범위를 생각하지 않았다.
    if i in L:
        pass
    elif i not in L:
        S.append(i)
print(min(S))
print(max(S))



문제="바구니 바꾸기" 
basket_num,change_num= map(int,input().split(" "))
#basket 만들기
L=[]
for i in range(basket_num):
    L.append(i+1)
for i in range(change_num):
    Fn,En=map(int,input().split(" "))
    if Fn+i == En-i:
        pass
    for i in range((En-Fn)//2+1):
# //(몫)을 이용하는 방법으로 구했다.
        L[Fn-1+i],L[En-1-i]=L[En-1-i],L[Fn-1+i]
for i in L:
    print(i, end=" ")
오래걸린_이유 = "리스트는 괄호를 결과로 보여준다."
정답= "프린터를 안해서 틀린 거임 리스트는 []에서만 나옴"



문제 = "평균내기"
subject_num= int(input())
L=list(map(int,input().split()))
sum=0

M_l=max(L)
for i in L:
    sum+= i/M_l*100
print(sum/subject_num)
