import random #or (from random import choice) from  is a keyword that is used to import a function from a module but in a  specific way 

coin=random.choice(["Heads","Tails"])
print("Result of coin tossed is:",coin)
#use of from keyword
from random import randint
number =randint(1,10)
print("Result of random integer choosen between 1 to 10 is:",number)
#use of shuffle function
cards=["jack","Queen","King"]
random.shuffle(cards)
print("shuffled sequence of card  is:")
for card in cards:
 print(card)
#importing statistics
import statistics
mean=statistics.mean([100,60,80,70])
print("The mean of the given number is:",mean)