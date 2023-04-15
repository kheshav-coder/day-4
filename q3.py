x=0
l=[]
while x<10:
    n=input("enter the name:")
    if n=="EXIT":
        break
    l.append(n)
    x+=1

print("the names you entered:")
print(*l,sep="\n")