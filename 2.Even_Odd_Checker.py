#WAP to enter 3 digit number and check the middle digit is even or odd
    
a= int(input("Enter 3 digits number")) #suppose 521

div = int(a/10)  #521/10=52
nmod = div%10   #52%10 = 2

if(nmod%2==0):
    print("Even")
else:
    print("Odd")


