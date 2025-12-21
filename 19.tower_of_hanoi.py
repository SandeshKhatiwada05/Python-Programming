#Tower of Honoi
#3 poles 3 ring in ascending order and put it in third ring with the help of second

def TowerOfHanoi(n , source, destination, auxiliary):
    if n==1:
        print ("Move disk 1 from source",source,"to destination",destination)
        return
    TowerOfHanoi(n-1, source, auxiliary, destination)
    print ("Move disk",n,"from source",source,"to destination",destination)
    TowerOfHanoi(n-1, auxiliary, destination, source)
         
# Driver code
n = 5
TowerOfHanoi(n,'Source','Auxiliary','Target')
