"""WAP to create class student having attribute id, name, address and conatct. Create constructor
getter and setter method. Create a class operation which contain the method to create the record of 
the student and a method to display all the records. Create a class program which contain some
main method which ask the user to enter the choice such as if the choice is 1 create the record of
the student, if the choice is 2 display allthe record otherwise terminate the program by displaying
a thankyou message."""

#Class creation
class student():
    def __init__(self,id,name,address,contact):
        self.id=id
        self.name=name
        self.address=address
        self.contact=contact

    def getID(self):
        return self.id
    
    def setID(self,id):
        self.id=id

    def getNA(self):
        return self.name
    
    def setNA(self,name):
        self.name=name

    def getAD(self):
        return self.address
    
    def setAD(self,address):
        self.address=address

    def getCO(self):
        return self.contact
    
    def setCO(self,contact):
        self.address=contact


class operation(student):
    def __init__(self):
        pass
    
    def create_student(self):
        id=int(input("Enter ID number: "))
        name=input("Enter Name: ")
        address=input("Enter Address: ")
        contact=input("Enter Contact: ")
        s=student(id,name,address,contact)
        return s
    
    def display_Record(self,s1):
        print("ID\t Name\t Address \t Contact")

        for s in s1:
            print(s.getID(),"\t",s.getNA(),"\t",s.getAD(),"\t",s.getCO())

class Main():
    def __init__(self,li):
        self.li=li

    def main(self):
        while(True):
            print("Enter 1 for Creating record")
            print("Enter 2 for Creating record")
            print("Enter any other key to stop")
            choice = int(input("Enter Your Chocie: "))
            o=operation()
            if(choice==1):
                s=o.create_student()
                self.li.append(s)
            elif(choice==2):
                o.display_Record(self.li)
            else:
                return 

m=Main([])
m.main()
    

        