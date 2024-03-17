def write():
    dog=input("What's your favorite dog breed ?\n")
    with open("dog.txt","+a") as file:
        file.write(f"{dog}\n")
def read():
    dogs=[]
    try:
        with open("dog.txt") as file:
            for line in file:
                #print("The list of dog breeds are:")
                dogs.append(line.rstrip())#to add dog breeds in list  
        print("The sorted list of dog breeds are:") 

        for dog in sorted(dogs,reverse=True):
            print(f"{dog}")
        
    except FileNotFoundError:
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
           