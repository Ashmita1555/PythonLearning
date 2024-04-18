class Faculty:
    def __init__(self,name):
        if not name:
            raise ValueError("Missing Name")
        self.name=name
    def display(self):
        print(f"My faculty is{self.name}")
class Student(Faculty):
    def __init__(self, name,house) :
        super().__init__(name)
        self.name=name 
        self.house=house
    def student(self):
        print(f"My name is  {self.name}from{self.house}")
class Professor(Faculty):
    def __init__(self, name,subject):
        super().__init__(name)
        self.name=name
        self.subject=subject
    def Subject(self):
        print(f"my name is {self.name}and my faculty is {self.subject}")
def main():       
    faculty=Faculty("Physics")
    stu=Student("Harry","Gryffindor")  
    pro=Professor("severus","Biology")            
    faculty.display()
    stu.student()
    pro.Subject()

if __name__=="__main__":
    main()