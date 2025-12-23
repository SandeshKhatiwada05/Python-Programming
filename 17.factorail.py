#Recursive funtion to find factorial

def fact(n):
    if(n!=1):
        return (n*fact(n-1))
    else:
        return 1

s=int(input("Enter a Number: "))
print(fact(s))

     
