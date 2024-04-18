class Student:
    def __init__(self ,name,house):
        self.name= name
        self.house= house
    def __str__(self):
            return f"{self.name} from {self.house}"
        
        
        
    @property#getter for name
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Missing Name")
        self._name=name
        
    @property#this is getter method ,to define it property is used
    def house(self):
        return self._house
    @house.setter
    def house(self,house):
        if house not in["kathmandu","lalitpur","bhaktapur","jhapa"]:
            raise ValueError("Invalid House")
        
        self._house=house

def main():
    student =get_student()
    print(student)
   
def get_student():
    
    name= input("Name: ")
    house= input("House: ")
    
    return Student(name,house)
    
    
if __name__=="__main__":
    main()    

    