from SelfCreatedlibraries import Calculation
x=int(input("Enter a number:"))
x1=int(input("Enter a number:"))
def main():
   
    test_square()
    x=int(input("Enter a number:"))
    x1=int(input("Enter a number:"))
def test_square():
    try:
        assert Calculation(x)==4
    except AssertionError:
        print(f"{x}square is not 4")
    try:    
        assert  Calculation(x1) ==9
    except AssertionError:
        print(f"{x1}square is not 9")
if __name__=="__main__":
    main()      