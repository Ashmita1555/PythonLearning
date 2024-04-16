#returning tuple and indexing .tupe is immutable
def main():
    student =get_student()
    if student["name"]=="sita":#it gives error as tuple is immutable
        student["city"]="jhapa"
    
    print(f"{student[0]} from {student[1]}")#for tuple
    
    student=get_student1()
    if student["name"]=="sita":
        student["city"]="jhapa"
    print(f"{student['name']} from {student['city']}")#for dictionary
    
    
#Tupel  
def get_student():
    name= input("Name:")
    city= input("City:")
    return (name,city)
#Dictionary
def get_student1():
    name=input("Name: ")
    city=input("City: ")
    return{"name":name,"city":city}
if __name__=="__main__":
    main()
    
    