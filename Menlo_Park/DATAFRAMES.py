from RESOURCE import ADDRESS as address
from RESOURCE import APARTMENTNAME as apartment
from RESOURCE import CITY as city
from RESOURCE import PRICE as price
from RESOURCE import BEDROOM as bedroom
import pandas as pd
import numpy as np

#DataFrames
mp=pd.DataFrame({
    'Apartment':apartment.apartmentName(),
    'Address':address.address(),
    'City':city.city(),
    })
#return mp
print(mp)

mpBed=pd.DataFrame({
    'Bedroom':bedroom.bedroom(),
    'Price':price.price(),
    })
#return mpBed
print(mpBed)

#CSV
df1mp=mp.to_csv(r'D:\Programming\Portfolio\Project 4 - Apartment\Menlo_Park\Apartment(Menlo_Park).csv')
df2mp=mpBed.to_csv(r'D:\Programming\Portfolio\Project 4 - Apartment\Menlo_Park\Bedroom(Menlo_Park).csv')
