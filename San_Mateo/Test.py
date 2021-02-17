from RESOURCE import ADDRESS as address
from RESOURCE import APARTMENTNAME as apartment
from RESOURCE import CITY as city
from RESOURCE import PRICE as price
from RESOURCE import BEDROOM as bedroom
import pandas as pd
import numpy as np

#Length:                                    DataTypes:
print(len(apartment.apartmentName()))   #24 str
print(len(address.address()))           #24 str
print(len(city.city()))                 #24 str (category)
print(len(bedroom.bedroom()))           #61 str (category)
print(len(price.price()))               #61 float

#Lists
#print((apartment.apartmentName()))  
#print((address.address()))           
#print((city.city()))                 
#print((bedroom.bedroom()))           
#print((price.price()))   
