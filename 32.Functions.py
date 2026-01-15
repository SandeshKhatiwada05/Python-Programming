"""Create a class base with attribute ID, Type, status, vechile, which inherits the base class and 
   contains the attirbute, description, manufacture date and Price. The class also contains the method to display
   all the information about the vehicle. Increase the price of each vehicle by 10% and display."""

class vehicle_info():
    def __init__(self,desc,manu_date,price):
        self.desc=desc
        self.manu_date=manu_date
        self.price=price

    def getd(self):
        return self.desc

    def setd(self,desc):
        self.desc=desc

    def getm(self):
        return self.manu_date
    
    def setm(self,manu_date):
        self.manu_date=manu_date

    def getp(self):
        return self.price
    
    def setp(self,price):
        self.price=price

class from_vehicle_info(vehicle_info):
    def __init__(self,id,type,status,vehicle,desc,manu_date,price):
        super().__init__(self,desc,manu_date,price)
        self.id=id
        self.type=type
        self.status=status
        self.vehicle=vehicle

    def getid(self):
        return self.id
    
    def setid(self,id):
        self.id=id

    def gettype(self):
        return self.type

    def settype(self,type):
        self.type=type

    def getstatus(self):
        return self.status
    
    def setstatus(self,status):
        self.status=status    

    def getvehicle(self):
        return self.vehicle

    def  setvehicle(self,vehicle):
        self.vehicle=vehicle

    def get_all_info(self):
        # we need self,id,type,status,vehicle,desc,manu_date,price
        id=input("Enter ID: ")
        type=input("Enter Type: ")
        status=input("Enter Status: ")
        vehicle=input("Enter Vechicle: ")
        desc=input("Enter Description: ")
        manu_date=int(input("Enter Manufacture Date: "))
        price=input("Enter Price(In Cr.): ")
        all=from_vehicle_info(self,id,type,status,vehicle,desc,manu_date,price)

    def display_info(self,s1):
        print("Ouput")

        for all in s1:
            print(all.getd(),"\t",all.getm(),"\t",all.getp(),"\t",all.getid(),"\t",all.gettype(),"\t",
                  all.getstatus(),"\t",all.getvehicle())

     

        

