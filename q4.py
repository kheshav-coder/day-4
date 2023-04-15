import random
d=[1,2,3,4,5,6]
a=random.choice(d)
b=random.choice(d)
c=0
while a!=b:
    print(f"the dices read: {a} {b}")
    a=random.choice(d)
    b=random.choice(d)
    c+=1
print(f"the number of tries: {c}")
