from RESOURCE import ADDRESS as address
from RESOURCE import APARTMENTNAME as apartment
from RESOURCE import CITY as city
from RESOURCE import PRICE as price
from RESOURCE import BEDROOM as bedroom
import pandas as pd
import numpy as np

#DataFrames
mountainview=pd.DataFrame({
    'Apartment':apartment.apartmentName(),
    'Address':address.address(),
    'City':city.city(),
    })
#return mountainview
print(mountainview)

mvBed=pd.DataFrame({
    'Bedroom':bedroom.bedroom(),
    'Price':price.price(),
    })
#return mvBed
print(mvBed)

#CSV
df1=mountainview.to_csv(r'D:\Programming\Portfolio\Project 4 - Apartment\Mountain_View\Apartment(Mountain_View).csv')
df2=mvBed.to_csv(r'D:\Programming\Portfolio\Project 4 - Apartment\Mountain_View\Bedroom(Mountain_View).csv')
