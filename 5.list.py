#list is created by using square bracket and can contain any data type

#use of list() constructor to create a new list 
def Brands():
    brand=list(("Hyundai","Toyota","Renault","BMW","Suzuki"))
    print(len(brand))#len ()function gives the lenth of a list
    print(brand)
 #for accessinf list items   
def AccessItems( ):
    vechilelist=["Alot","Grand i10","Hylux","Duster"]
    print("\n These are the list of vehicle present now.")
    for i in range(len(vechilelist)):
        print(i+1,vechilelist[i])
    print("output printing using the positive index along with range",vechilelist[0:3])
    print("output using negative indexing and range\n",vechilelist[-1:-3])
    
 #changing list items   
def ReplaceValue( vechile):
     
     print("Replacing the item using indexing :")
     vechile[1:3]=["Seltos","Tucson"]
     print(vechile)
#Adding value items in list  without replacing using insert() fuction    
def InsertValue( vechile):
     index=int(input("enter the index of your choice: "))
     item=input("Enter the intems you want to add: ")   
     vechile.insert(index-1,item)
     print(vechile)

#adding at the end of the list 
def AddValue( vechile):
     item=input("Enter the item you want to add :- ")
     vechile.append(item)
     print(vechile)
     
#To append elements from another list to current list 
def Extend( vechile):
     
     fruits = ["apple", "banana", "cherry"]  
     vechile.extend(fruits)#entend fuction can append any iterable object(tuples,sets,dictionaries etc.)
     print(vechile)

#removing list items
def RemoveItems(vechile):
    choice=int(input("Enter your choice :\n 1.for pop fuction\n 2. for remove function\n 3.for clear function\n 4.for del function\n"))
    if choice==1:
        index=int(input("enter the index of the item you want to remove:\n"))
        vechile.pop(index-1)
        print(vechile)
    elif choice==2:
        item=input("Enter the item you want to remove\n")
        vechile.remove(item)
        print(vechile)
    elif choice==3:
           vechile.clear()
           print(vechile) 
    else:
        del vechile

def main():
    vechile=["Alot","Grand i10","Hylux","Duster"]
    print("choose option:\n 1. For knowing the brands\n 2.For accessing items\n 3.Replacing value\n 4.Inserting value in specified position \n 5.For adding a value\n 6.For ading another list to the existing list \n 7.For removing ,poping,clearing and deleting a list \n 8.Enter anyhing for termination.\n")
    while True:
        ch=int(input("Enter your choice: "))
        if ch==1:
            Brands()
        elif ch==2:
            AccessItems( )
        elif ch==3:
            ReplaceValue( vechile) 
        elif ch==4:
             InsertValue( vechile)
        elif ch==5:
               AddValue( vechile)
        elif ch==6:
            Extend( vechile)
        elif ch==7:
             RemoveItems(vechile)
    
        else:
            print("End of program!!!!") 
            break  
main()            
                               
        
    