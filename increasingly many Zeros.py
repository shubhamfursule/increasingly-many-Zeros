k=[]
for x in range(0,20):
    k.append(1)
    if x<=10:
        for y in range(0,x):
            k.append(0)
    else:
        break
print(k)

