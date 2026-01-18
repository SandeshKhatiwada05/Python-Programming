#Styles for Printing
print("He is a \"Good Boy\" ")
print("He\'s", 9, "yrs", 2, "months", sep="~") #sep seperates the object
print("I love you", 3000, end=" RIP TONY") #End specifies what to print at end

#Click on Alt and use as multiple cursor
#Click on Alt and down/up arrow to move some text

#Multiple line string
about ="""Hello Everyone!
My name is Sandesh. 
I am in Bachelor's 3rd semester."""
print(about)

#Lenght
name ="Mango"
l1= len(name)
print("Mango is a", l1, "letters word.")

#String part 
name="Saisa,Sandesh"
print(name[0:9])
print(name[0:-3]) #it means form zero to len(name)-3 i.e. 13-3=10
print(name[-5:-2]) #name[len(name)-5: len(name)-2]
print(name.upper()) #lower case into upper. P.S.Srings are immutable(change nahune)

#Additional
text = "!!!It can only remove from back!!!"
print(text.rstrip("!"))
print(text.replace("It can only remove from back", "I could Replace it")) #replaces
print(text.split()) #Splits into lists, it converts space into different lists
text= "i aM frOM nepAL"
print(text.capitalize()) #Manages text and makes first one capital
print(text.center(50)) #Manages alignment as needed
print(text.count("a")) #counts number of used character or string
print(text.swapcase()) #Swaps capital to small and small to capital

# lets=["man", "lan", "wan"]
# for let in lets:
#     print(let)
#     for x in let:
#         print(x) 