#for handeling error and exception in python we have try and except statement
def main():
    x=get_int("Enter the value of x :")
    
    if (x%2==0):
          print(f"The value of x is {x} and is  a even number.")        
    else:
          print(f"The value of x is {x} and is  a odd number.") 
def get_int(num):
    while True:
        try:
            return int(input(num))
   
    #valueError
        except ValueError:
           # print("THe value of x is not an Integer. Plz, give an integer value") 
           pass   
main()