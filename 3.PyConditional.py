#if else condition
score=int(input("Enter your Score:"))
if score>=90 and score<=100:
    print("Grade:A ")
elif score>=80 and score<90 :
    print("Grade:B")
elif score>=70 and score<80:
    print("Grade:C")
elif score>=60 and score<70:
    print("Grade:D")
elif score>=50 and score<60:
    print("Grade:E")
else:
    print("Grade:F")
    
    
#parity(checking even or odd)
def main():
    X=int(input("Enter the number:"))
    if parity(X):
        print(f"The  number {X} is even")
    else:
        print(f"The number {X} is even")   
def parity(n): 
 if n%2==0:
    return True
 else:
   return False

main()

# use of match similar to swith case
name=input("Enter your name:")
match name:
    case"Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case"Draco":
        print("Slyrherin")
    case _: #for exception
        print("Not recognized")    
    

     
        