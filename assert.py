x1=int(input("Enter  first  number:"))
x2=int(input("Enter Second Number:"))
def main():
    rectangle_area(x1,x2)
def rectangle_area(a,b):
    try:
        assert x1>0, " Negative number entered" #assert key word takes input as a boolean condition , if true then further execution else stops the execution and returns assertion error
        assert x2>0," Negative number entered"
        area=x1*x2
        print("Area of rectangle is:",area)
    except AssertionError:
        print("please enter a positive number")
if __name__=="__main__":
    main()
    
    