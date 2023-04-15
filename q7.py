n=int(input("enter the number >>>"))
s=[0,1]
while s[-1]<n:
    s.append(s[-1]+s[-2])
s.pop(-1)
print(*s)
