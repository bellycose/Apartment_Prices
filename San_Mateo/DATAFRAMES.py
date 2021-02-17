from RESOURCE import ADDRESS as address
from RESOURCE import APARTMENTNAME as apartment
from RESOURCE import CITY as city
from RESOURCE import PRICE as price
from RESOURCE import BEDROOM as bedroom
import pandas as pd
import numpy as np

#DataFrames#1
sanmateo=pd.DataFrame({
    'Apartment':apartment.apartmentName(),
    'Address':address.address(),
    'City':city.city(),
    })
#return sanmateo
print(sanmateo)

#DataFrames#2
sanmateoBed=pd.DataFrame({
    'Bedroom':bedroom.bedroom(),
    'Price':price.price(),
    })
#return sanmateoBed
print(sanmateoBed)

#CSV
df1sm=sanmateo.to_csv(r'D:\Programming\Portfolio\Project 4 - Apartment\San_Mateo\Apartment(San_Mateo).csv')
df2sm=sanmateoBed.to_csv(r'D:\Programming\Portfolio\Project 4 - Apartment\San_Mateo\Bedroom(San_Mateo).csv')


