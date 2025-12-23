"""WAP to ask a student name, his mark in five different subjects(without loop), find his total marks,
  pass fail category and division. Full mark=100, pass=35"""

name = input("Enter Name: ")
print("Entere your mark")
dsa =  float(input("DSA:              "))
stat = float(input("Statistics:       "))
nm   = float(input("Numerical Method: "))
cg   = float(input("Graphics:         "))
ca   = float(input("CA:               "))
total = dsa+stat+nm+cg+ca
per= (total/500)*100

if(dsa<35 or stat<35 or nm<35 or cg<35 or ca<35):
    print(name, "you're", "Fail!!")
else:
    print("Your Total marks is ", total)
    print("Your Percentage is ",((total/500)*100),"Percentage")
    if(per>=80 and per<100):
     print("Distinction")
    elif(per>=70 and per<80):
     print("1st Division")
    elif(per>=60 and per<70):
      print("2nd Divison")
    else:
     print("Just Pass")




 




