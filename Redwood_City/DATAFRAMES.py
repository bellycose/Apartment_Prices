from RESOURCE import ADDRESS as address
from RESOURCE import APARTMENTNAME as apartment
from RESOURCE import CITY as city
from RESOURCE import PRICE as price
from RESOURCE import BEDROOM as bedroom
import pandas as pd
import numpy as np

#DataFrames
rc=pd.DataFrame({
    'Apartment':apartment.apartmentName(),
    'Address':address.address(),
    'City':city.city(),
    })
#return rc
print(rc)

rcBed=pd.DataFrame({
    'Bedroom':bedroom.bedroom(),
    'Price':price.price(),
    })
#return rcBed
print(rcBed)

#CSV
df1rc=rc.to_csv(r'D:\Programming\Portfolio\Project 4 - Apartment\Redwood_City\Apartment(Redwood_City).csv')
df2rc=rcBed.to_csv(r'D:\Programming\Portfolio\Project 4 - Apartment\Redwood_City\Bedroom(Redwood_City).csv')
