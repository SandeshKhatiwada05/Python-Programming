#WAP to find two sum problem

target=int(input("Input Target: "))
lists=[]
n=int(input("Enter Number of Imputs to be taken: "))
for i in range(0,n):
    print("Enter Numbers in Lists: ")
    put=int(input("Number: "))
    lists.append(put)
print(lists)

for i in range(len(lists)-1,-1,-1):
    for j in range(1,i+1):
        if(lists[j-1]+lists[j]==target):
            print("Target Found")
        
    
