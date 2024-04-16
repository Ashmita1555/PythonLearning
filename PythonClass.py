class Student:
    def __init__(self ,name,city,age):
        if not name:
            raise ValueError("Missing name")
        if city not in ["kathmandu","bhaktapur","lalitpur"]:
            raise ValueError("Invalid City")
        self.name= name
        self.city= city
        self.age= age
    def __str__(self):
            return f"{self.name} from {self.city}"
    def hobby(self):#self created method
        match self.age:
            case "25":
                return"📔"
            case "20":
                return"💃"
            case "30":
                return "🎶"
            case _:
                return"🙁"
        
        
def main():
    student =get_student()
    
    print("Hobbies")
    print(student.hobby())
def get_student():
    
    name= input("Name: ")
    city= input("City: ")
    age=input("age: ")
    return Student(name,city,age)
    
if __name__=="__main__":
    main()