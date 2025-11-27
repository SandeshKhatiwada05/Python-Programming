#REGARDING STRING
Style_string = "Sandesh is my name."
multiline_string ='''Hello My name is Sandesh \nI am Sandesh'''
print(Style_string, multiline_string)
print("Sandesh " *5)  #multiple prints without using loop



#REGARDING CONDITIONS
c=2
d=4
e=6
if(c>d and c>e):
    print("c is greater")
elif(d>c and d>e):
    print("d is greater")
else:
    print("e is greater")




#REGARDING LOOP
for i in range(1,11):
    if i%2==0:
        print(i,"is Even")
    else:
        print(i,"is Odd")

for i in range(20,40,5): #same as above but 3rd part shows interval between them
    print(i)        



#THIS IS A SINGLE LINE COMMENT
"""This is a
multi line comment"""



#DICTIONARY IN PYTHON, SAME AS SWITCH IN C/C++ BUT EASIER
mydict = {
    "1" : "One",
    "2" : "Two",
}
print(mydict["1"])



#SETS AND LISTS
set = {1,2,4,5,1} #It doesn't read repeated values
print(set)
list = [1,2,3,1] #It reads repeated values
print(list)
list.append(10) #Append => add a new number
print(list)
tp =(1,2,3,4) #Tuple objects cannot be changed i.e. tp[0]=3 doesn't exists



#MATHEMATICS BASIC CALCULATIONS
print(5/2) #gives float value
print(5//2) #gives integer value or,
print(int(5/2)) #gives intger value
print(2**3) #gives power
print(type(5/2)) #gives type 
print(type(2+3j)) 



#CONVERSION OF NUMBER SYSTEM
a=20
print("Binary of 20 is", bin(a))
print("Octal of 20 is", oct(a))
print("Hexadecimal of a is", hex(a))



#FOR BASIC MATHS 
import math
print("Ceiling of 5.2 is ", math.ceil(5.2))
print("Floor of 5.2 is ", math.floor(5.2))
print("After maths library pow(5,2) works i.e.", pow(5,2))


#FOR FUNCTION
"""a=6
def divisivleby(num,r):
    if num%r==0:   #num and r can be any value
        return True
    else:
        return False"""
    
