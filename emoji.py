def convert(output):
       
  emoji={":)":"🙂",":(":"🙁"}
  
  for x ,y in emoji.items():
         output =output.replace(x,y)
  print(output)
       
      
def main():
       output=input("Enter a sentence:")
       convert(output)
main() 

      
        
        