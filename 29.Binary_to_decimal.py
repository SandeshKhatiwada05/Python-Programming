#WAP to ask binary and convert it to decimal

def into_binary(n,a):
    st=0
    for i in range(0,len(str(n))):
        r=n%10
        st=st+r*(2**i)
    print(st)
        
        
into_binary(1110,2)

