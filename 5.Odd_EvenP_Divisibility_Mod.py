"""WAP to ask user enter 3 digit numbers. If the entered number is divisible by 6.Then check the last 
digit if it is divisible by 3 or not. If not divisible by 6 , check the middle digit is odd or even"""

a=int(input("Enter 3 digit numbers: "))
#156
last=a%10
formiddle=int(a/10)   #15
middle=formiddle%10    #5

#Checking divisivle by 6
if (a%6==0):
    print("It is divisble by 6 \nSo checking if last number is divisible by 3")
   
    if(last%3==0):
        print("Last number is also divisble by 3. \n")
        
    else:
        print("Last Number is not divisble by 3")

#not divisible by 6       
else:
    if(middle%2==0):
        print("It is even")
    else:
        print("Odd")

