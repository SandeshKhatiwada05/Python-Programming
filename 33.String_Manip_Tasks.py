#WAP to ask  a string input and display it as follow: H$E$L$L$O

a=input("Enter a string: ")
n=len(a)
st=""
for i in range(n):
    st=st+a[i].upper()+"$"  #H$E$L$l$O$
print(st[0:len(st)-1])      #H$E$L$l$O
    
