even=[]
odd=[]
for i in range(51):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even,end=',')
print(odd)
