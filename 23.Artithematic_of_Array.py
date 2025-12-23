#WAP to add 10 different integers in a list. Display sum of all even numbers and odd numbers

def takenum():
    a=int(input("Enter number: "))
    return a


def main():
    lists=[]
    even=0
    odd=0
    for i in range(0,10):
        lists.append(takenum())
    print(lists[i])
    
    for i in lists:
        if(i%2==0):
            even=even+i
            return even
        else:
            odd=odd+i
            return odd
    print("Even is ",even)
    print("Odd is ",odd)
        
main() 