import re
name=input("Enter your name:").strip()
if matches := re.search(r"^(.+), *(.+)$",name):#(:= assign the value as well as ask a boolean question)
    name=matches.groups(2)+" "+matches.groups(1)
    
print(f"hello,{name}")