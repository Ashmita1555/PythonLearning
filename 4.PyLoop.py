"""Two loops in python:-
i.while
ii.for"""
#while loop
i=0
while i<5:
    print("Hello There!!!")
    i+=1
#for loop
for i in range(6):
    print("Meow")
for _ in range(5):
    print("Hello!!")
#can also be done
print("meow\n"*3, end="")
#user input as range
while True:#infinite loop
    n=int(input("Whats n?"))
    if n>0:
        break
for _ in range(n):
    print("meow")
    
#loop having function
def main():
    number=get_number()
    meow(number)
def get_number():
    while True:
        n=int(input("what's n?"))
        if n>0:
            break
    return n 
def meow(n):
    for i in range(n):
     print("meow")