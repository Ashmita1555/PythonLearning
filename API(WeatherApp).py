import json
import requests
api_key="42d0aaf155279da37c9434b141e8f5f2"
for i in range(5):
    User_input=input("Enter city: ")
    print(User_input)
    Weather_data=requests.get(  f"https://api.openweathermap.org/data/2.5/weather?q={User_input}&units=imperial&APPID={api_key}" )   
#print(Weather_data.json())#to print the whole data of the url

    if Weather_data.json()['cod']=='404':
           print("City Not Found")
    else:    
        weather = Weather_data.json()['weather'][0]['main']
        temp=Weather_data.json()['main']['temp']
        print( f"The weather of the {User_input} is:{weather}")
        print(f"The temperature is:{temp}°F")