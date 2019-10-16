# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 12:02:41 2019

@author: BSDU ADMIN
"""

import requests
from datetime import datetime
import time

city=input("Enter the city for temperature  :")

url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q="+city
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"

url=url1+url2+url3

response=requests.get(url)

response.content

json_data=response.json()


print("Temperature of {} is {} Celsius .".format(city.upper(),round(json_data["main"]["temp"]-273.15,2)))
print("Sunrise at {} is at {}am .".format(city.upper(),datetime.fromtimestamp(json_data["sys"]["sunrise"])))
print("Sunset at  {} is at {}pm .".format(city.upper(),datetime.fromtimestamp(json_data["sys"]["sunset"])))
print("Wind speed of  {} is {} .".format(city.upper(),json_data["wind"]["speed"]))


#OR
"""
print("Sunrise at {} is at {}am .".format(city.upper(),datetime.fromtimestamp(json_data["sys"]["sunrise"])))
print("Sunset at  {} is at {}pm .".format(city.upper(),datetime.fromtimestamp(json_data["sys"]["sunset"])))

"""