def main():
    temp1=float(input("Enter the temperature into celsius:"))
    temp2=float(input("Enter the temperature in farenheit:"))
    celsius_to_farenheit(temp1)
    farenheit_to_celsius(temp2)
def celsius_to_farenheit(t1):
    temp1 =((t1/5)*9)+32
    print(" Celsius converted to Farenheit:",temp1)
def farenheit_to_celsius(t2):
     temp2=((t2-32)*5)/9 
     print(" Farenheit coverted to Celsius:",temp2) 
if  __name__ =="__main__" :      
   main()        