# 개수부터 
# count
# 위치의 번호를 넣기
# find
#4949
import sys
n= sys.stdin.readline().rstrip()
s="no"
n1=n.count("(")
n2=n.count(")")
n3=n.count("[")
n4=n.count("]")
if n1!=n2:
    print(s)
elif n3!=n4:
    print(s)
else:
    while True:
        n_num1=n.find("(")
        n_num2=n.find(")")
        if n_num1 != -1 or n_num2!=-1:
            if n_num1<n_num2:
                n=n.replace("(","")
                n=n.replace(")","")
            else:
                print("no")
                break
        else:
            break

    while True:
        n_num1=n.find("[")
        n_num2=n.find("]")
        if n_num1!=-1:
            if n_num1<n_num2:
                n=n.replace("[","")
                n=n.replace("]","")
            else:
                print("no")
                break
        else:
            print("yes")
            break