import csv
def write():
    name=input("What's your pet name  ?\n")
    family=input("What's your pet breed  ?\n")
    with open("dog.csv","a", newline='') as file:
           writer=csv.DictWriter(file, fieldnames=["name", "family"])
           writer.writerow({"name":name,"family":family})
                   
def read():
        dogs=[]
        try:
            with open("name.csv")as file:
                reader=csv.DictReader(file)
                for row in reader:
                    dogs.append({"name":row["name"],"family":row["family"]})
        
            for dog in sorted(dogs, key = lambda x:x["name"]):
                print(f"{dog['name']}is of family{dog['family']}") 
           
        except FileExistsError:
               print("No file created.Plz!! create a file.")                 
def main():
    for _ in range(5):
        choice=int(input("Enter your choice.\n 1 for write \n 2 for read.\n 3 for exit.\n"))
        if choice==1:
            write()
        elif choice==2:
            read()
        elif choice==3:
            exit()
        else:
            print("Pls enter a valid choice.")
if __name__=="__main__":
    main()