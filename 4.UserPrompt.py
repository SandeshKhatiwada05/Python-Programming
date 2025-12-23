"""WAP to find sum, difference, product of 3 user input numbers. Find the sum only if, the first number 
is the middle number, difference only if second number is the middle number and product 
only is the last number is the middle number"""

a= int(input("Enter First Number: "))
b= int(input("Enter Second Number: "))
c= int(input("Enter Third Number: "))

#for first number to be middle number
#b>a>c or c>a>b
if((b>a and a>c) or (c>a and a>b)):
    print("Sum is", a+b+c)


#second number to be middle number
#a>b>c or c>b>a
elif((a>b and b>c) or (c>b and b>a)):
    print("Difference is ", a-b-c)  #addition


 #third number to be middle number
else:
    print("Product is ", a*b*c)  #multiplication   


