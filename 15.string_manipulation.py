"""WAP to ask user a sentence from the user and change the case afternatively, stating from upper case
  for eg: this is a line-->ThIs iS A LiNe"""

s=input("Enter Your sentence ")
lens=len(s)
for i in range(0,28):
    rev = i

for i in range(-1, -(len(s)-1),-1):
    if(i%2!=0):
        rev=rev+s[i].upper()
    else:
        rev =rev+ s[i].lower()
    print(rev)
