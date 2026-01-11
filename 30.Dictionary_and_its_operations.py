"""WAP to enter number of records to be stored in a dictionary. The records must be the detais of the 
   students i.e. (id,Name,Address,contact).Store the record in dictionary as given below:
   {'ID'[.....],'Name'[.....],....} """

id_list=[]
name_list=[]
address_list=[]
contact_list=[]
d={}  #dictionary


def main():
 n=int(input("How many Inputs do you want to input?: "))
 for i in range(0,n):
  name=input("Enter Name of the person: ")
  name_list.append(name)
  id=input("Enter ID of the person: ")
  id_list.append(id)
  add=input("Enter Address of the person: ")
  address_list.append(add)
  contact=input("Enter contact of the person: ")
  contact_list.append(contact)
  
  #Dictionary
  d['ID']=id_list
  d['NAME']=name_list
  d['ADDRESS']=address_list
  d['CONTACT']=contact_list
 print(d)
    

main()
  





"""first mai d={ 'id' [], 'Address' [], 'contact' []}
ani last ma append garda d['Name_list'],append(name)"""  



