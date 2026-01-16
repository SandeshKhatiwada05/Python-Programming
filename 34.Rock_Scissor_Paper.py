#Scissor, Paper, Rock

print("Scissor, Paper, Rock game")
print("1 for Scissor\n2 for Paper\n3 for Rock")
print("Player one, Your move!!")
a=int(input(""))
if(a==1):
    print("You Typed Scissor")
elif(a==2):
    print("You Typed Paper")
elif(a==3):
    print("You Typed Rock")
print("Player Two, You Goo!!")
b=int(input(""))
if(b==1):
    print("You Typed Scissor")
elif(b==2):
    print("You Typed Paper")
elif(b==3):
    print("You Typed Rock")
if(a==1 and b==2):
    print("Player 1 wins")
elif(a==1 and b==3):
    print("Player 2 wins")
elif(a==1 and b==1):
    print("Tie")
elif(a==2 and b==1):
    print("Player 2 wins")
elif(a==2 and b==2):
    print("Tie")
elif(a==2 and b==3):
    print("Player 2 wins")
elif(a==3 and b==1):
    print("Player 1 wins")
elif(a==3 and b==2):
    print("Player 2 wins")
elif(a==3 and b==3):
    print("Tie")
