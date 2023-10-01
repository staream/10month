
L=[]

a= "1 1 1"
#a= int(a.split())# 불가능
#m__a= map(int,a.split()) 불가능
#a,b = map(int,a.split()) 가능
L.append(a)
print(L)
b =a.split()
L.append(a.split())
print(L)
print(b)
a= map(int,input().split())
print(a)


s= "123"
print(s[4])