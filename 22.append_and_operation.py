#WAP TO create a list. Add the name of your 5 friends. Display all names in reversed order 

# print("Name of your five friends:\n")
# one=input("First: ")
# two=input("Second: ")
# three=input("Third: ")
# four=input("Fourth: ")
# five=input("Fifth: ")
# lists=[one,two,three,four,five]
# print(lists)

#also also
#Declaring name first
def takename():
    name=input("Enter name: ")
    return name

#Function for reversing
def reverse_string(input_str):
    if len(input_str) == 0:
        return input_str
    else:
        return reverse_string(input_str[1:]) + input_str[0]
    
#Function to print list back and front
def reverse_list(s):
    st=""
    for i in range(s)-1,-1,-1:
        st=st+s[i]
    return st     

    

def main():

    lists=[]
    for i in range(0,5):
        lists.append(takename())

    print("Names are: ")
    print(lists) 
    print("\nFor Revrsing names: ")
    
    newlist=[]
    print("New List is:")
    for i in range(0,5):
        print(newlist.append(reverse_string(lists[i])))
    
        
        
main() 



