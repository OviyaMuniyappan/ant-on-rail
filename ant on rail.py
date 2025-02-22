#ant on rail..
n=int(input("enter: "))
l=list(map(int,input().split()))
pos=0
neg=0
for i in range(len(l)-1):
    if(l[i]==1):
         pos+=1
    else:
        neg+=1
print(min(pos,neg))