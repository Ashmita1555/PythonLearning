#Dictionary used to store data value in key: value pairs. Duplication not allow and are written with curly bracket

#simple dictionary
def dict():
    dictionary={"Ashmita":"GreenHouse",
            "Ashwin":"YellowHouse",
            "Anjal":"BlueHouse",
            "Subodh":"RedHouse"
    }
    print(dictionary)#simple way of printing dictionary 
    print(dictionary["Ashmita"])#prints value of key Ashmita
    for student in dictionary:
        print(student)#prints key only
    for student in dictionary:
        print(student,dictionary[student], sep=" ,")#prints both key and value
        
def UpdateDictionary():
    Udict={"s1":"ashmita","s2":"susmita","s3":"anjal"}
    #add the new key value pair  at last in the dictionary
    Udict["s4"]="rohan"
    Udict.update({"s5":"ashwin"}) 
    Udict.update({"s3":"subodh"})#update the value of s3 as subodh
    print(Udict)
    
def NestedDictionary():#dictionary within dictionary
    MySibilings={
        "sib1":{
            "name":"Ron",
            "age": 15
                   },
        "sib2":{
            "name":"Draco",
            "age":20
        },
        "sib3":{
            "name":"Anju",
            "age":25
        },
               }
    print(MySibilings["sib2"]) 
def Multivalued():#list haveing multiple dictionary as its items.
    EmployeeDetails=[
        {"name":"Radha","address":"khumaltar","post":"SalseManager"},
        {"name":"Shyam","address":"Dhapakhel","post":"BranchManager"},
        {"name":"Geeta","address":"sanepa","post":"Accountant"}
     ]
    #accessing name only 
    print("Displaying name of the employee:\n ")
    for employee in EmployeeDetails:
        print(employee["name"])
    #accessing all the details
    print("Displaying all the details\n") 
    for employee in EmployeeDetails:
        print(employee["name"],employee["address"],employee["post"],sep= ",") 
          
    
def main():
    dict()
    UpdateDictionary()
    NestedDictionary()
    Multivalued()
main()
