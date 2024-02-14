"""function in python  is defined using def 
indentation is important """
#defining function
def hello():
    print("Hello!!!")
name=input("what's your name?")
hello()
print(name)

#parameter in function
def hello(to):
    print("Hello!!!",to)
name=input("what's your name?")
hello(name)

# passing  value as default in parameter
def hello(to="world"):
    print("Hello!!!",to)
name=input("what's your name?")
hello(name)
 
#main funtion
def main():
    name=input("what's your name?")
    hello(name)
    x=int(input("Enter the value:"))
    print(f"{x} square is",squared(x))
def squared(n):
    # use of return keyword
    return pow(n,2)
def hello(to="world"):
      print("Hello!!",to)

main()




        
