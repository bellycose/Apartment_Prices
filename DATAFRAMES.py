import pandas as pd
import numpy as np
#Imports
#Redwood City
dfrc=pd.read_csv(r'Redwood_City\Apartment(Redwood_City).csv',index_col=0)
bdrc=pd.read_csv(r'Redwood_City\Bedroom(Redwood_City).csv',index_col=0)
#Menlo Park
dfmp=pd.read_csv(r'Menlo_Park\Apartment(Menlo_Park).csv',index_col=0)
bdmp=pd.read_csv(r'Menlo_Park\Bedroom(Menlo_Park).csv',index_col=0)
#Mountain View
dfmv=pd.read_csv(r'Mountain_View\Apartment(Mountain_View).csv',index_col=0)
bdmv=pd.read_csv(r'Mountain_View\Bedroom(Mountain_View).csv',index_col=0)
#San Mateo
dfsm=pd.read_csv(r'San_Mateo\Apartment(San_Mateo).csv',index_col=0)
bdsm=pd.read_csv(r'San_Mateo\Bedroom(San_Mateo).csv',index_col=0)
'''
This file will manage data from list to dataframe and analyze with statistics.
'''

#Population Bedroom Available
frame=[bdrc,bdmp,bdmv,bdsm]
result=pd.concat(frame)
#print("Vacancy in all selected Apartments:\n",result)
popPrices=result["Price"]
pop=popPrices.describe()
print(f'Population:\n{pop}\n')

#Sample Bedroom Available - 
bdrcPrice=bdrc.describe()
bdmpPrice=bdmp.describe()
bdmvPrice=bdmv.describe()
bdsmPrice=bdsm.describe()

print(f'Redwood City:\n{bdrcPrice}\n')
print(f'Menlo Park:\n{bdmpPrice}\n')
print(f'Mountain View:\n{bdmvPrice}\n')
print(f'San Mateo:\n{bdsmPrice}\n')

#Quantile
df=pd.DataFrame(result)
dfrc=pd.DataFrame(bdrc)
dfmp=pd.DataFrame(bdmp)
dfmv=pd.DataFrame(bdmv)
dfsm=pd.DataFrame(bdsm)

boxpop=df['Price'].quantile([0.25,0.50,0.75])#Quartiles of Price
boxrc=dfrc['Price'].quantile([0.25,0.50,0.75])
boxmp=dfmp['Price'].quantile([0.25,0.50,0.75])
boxmv=dfmv['Price'].quantile([0.25,0.50,0.75])
boxsm=dfsm['Price'].quantile([0.25,0.50,0.75])

print(f'Population:\n{boxpop}\n\n\
Redwood City:\n{boxrc}\n\n\
Menlo Park:\n{boxmp}\n\n\
Mountain View:\n{boxmv}\n\n\
Redwood City:\n{boxsm}\n\n')
