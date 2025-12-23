#Bubble sort

l=[23,45,26,67,89,29]
print(l)
for i in range(len(l)-1,-1,-1):
    for j in range(1,i+1):
        if(l[j-1]>l[j]):
            l[j-1],l[j]=l[j],l[j-1]
print(l)
