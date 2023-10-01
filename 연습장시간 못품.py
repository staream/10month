n= int(input())
L=[]
for i in range(1000000):
    L.append(0)
for i in range(n):
    a= int(input())
    L[a-1]=a
for i in L:
    if i ==0:
        pass
    else:
        print(i)
