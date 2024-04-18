import random
class Hat:
    houses=["Green","Red" ,"Blue","Yellow"]
    
    @classmethod
    def sort(cls,name):
        print(name,"is in",random.choice(cls.houses),"house.")
Hat.sort("Harry")