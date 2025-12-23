#reverse string using negative indexing

s=input("Enter a Sentence")
for i in range(1,-len(s),-1):
    print(s[i], end="")