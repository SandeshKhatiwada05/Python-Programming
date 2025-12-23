#Pattern Printing   

n=5
for i in range(n):
    print("*")


for i in range(n):
    print("*", end="")    



#also as
print("\n")               
print("*"*5, end="")     



for i in range(n):
    for j in range(n):
        print("*",end="")



for i in range(n):
    for j in range(n):
        print("*",end="")
    print("\n")               



#for increasing order
print("For increasing: ")
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()    



#decreasing star
print("For decreasing: ")
for i in range(n):
    for j in range(i,n):
        print("*",end="")
    print("")      



#Trinagle
print("\n\nNow we print triangle\n\n")
for i in range(n):
    for j in range(i,n):
        print(" ",end="")

    for j in range(i+1):
        print("*",end="")  
    
    for j in range(i+1):
        print("*",end="")
    print()    



#Diamond
print("\n\nNow we Print Diamond\n\n")
for i in range(n):
    for j in range(i,n):
        print(" ",end="") 

    for j in range(i+1):
        print("*",end="")

    for j in range(i+1):
        print("*",end="")    
    print()       

for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n):
        print("*",end="")    
    for i in range(i,n):
        print("*",end="")    
    print()    
       


#More accurate Diamond
for i in range(n-1):
    for j in range(i, n-1):
        print(" ", end="") 

    for j in range(i):
        print("*", end="")

    for j in range(i+1):
        print("*", end="")    
    print()       

for i in range(n):
    for j in range(i+1):
        print(" ", end="")
    for j in range(i, n):
        print("*", end="")    
    for k in range(i, n-1):   
        print("*", end="")    
    print()
