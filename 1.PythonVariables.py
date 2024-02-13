"""Variables are the container for storing data value 
In python we donot have specified command for declaring a variables ,we create them whenever we assign a value on it.
num=10
name="ashmita"
x='timalsina'
"""

#ways of getting user input 
Name=input("Enter your name:")#by default takes string
Num=int(input("Enter your age:"))#for integer value
weight=float(input("Enter your weight:"))#for float value

#remove whitespace from str and capitalization
Name=Name.strip().title()

#splits user's name into first name and last name
first,last =input("Enter your fullname:").split()

#printing method
print(f"Name:{Name}")#print value using format string
print(f"split user's first name as output:{first} ")
print(f"split user's last name as output:{last} ")
print("Age:",Num)
print("Weight:",weight)
# to round the float value
z=Num+weight
round(z,2)
#OR
print(f"{z:.2f}")
#seperate large no by comma
print(f"{z:,}")