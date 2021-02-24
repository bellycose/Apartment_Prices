import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

#Population from each cities
frame=[bdrc,bdmp,bdmv,bdsm]
result=pd.concat(frame)

#Create Arrays
dfpop=np.array(result['Price'])
dfRC=np.array(bdrc['Price'])
dfMP=np.array(bdmp['Price'])
dfMV=np.array(bdmv['Price'])
dfSM=np.array(bdsm['Price'])

#Sorted in Order
pop=sorted(dfpop)
RC=sorted(dfRC)
MP=sorted(dfMP)
MV=sorted(dfMV)
SM=sorted(dfSM)

#Length
#print(len(pop))#207
#print(len(RC))#50
#print(len(MP))#36
#print(len(MV))#60
#print(len(SM))#61

#Calculate for 10% Trimming
xpop=len(pop)*.10
xrc=len(RC)*.10
xmp=len(MP)*.10
xmv=len(MV)*.10
xsm=len(SM)*.10

#print(round(xpop))#21 both sides
#print(round(xrc))#5 both sides
#print(round(xmp))#4
#print(round(xmv))#6
#print(round(xsm))#6

#Trim at 10%
trimpop=pop[21:-21]
trimrc=RC[5:-5]
trimmp=MP[4:-4]
trimmv=MV[6:-6]
trimsm=SM[6:-6]

#Convert List to Data Frame
v=pd.DataFrame(trimpop).describe()
w=pd.DataFrame(trimrc).describe()
x=pd.DataFrame(trimmp).describe()
y=pd.DataFrame(trimmv).describe()
z=pd.DataFrame(trimsm).describe()

#Summary at 10% Trim
print(f'Population 10%:\n{v}\n\n\
Redwood City 10%:\n{w}\n\n\
Menlo Park 10%:\n{x}\n\n\
Mountain View 10%:\n{y}\n\n\
San Mateo 10%:\n{z}\n\n')
