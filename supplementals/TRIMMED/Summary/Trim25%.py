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

#Calculate for 25% Trimming
xxvpop=len(pop)*.25
xxvrc=len(RC)*.25
xxvmp=len(MP)*.25
xxvmv=len(MV)*.25
xxvsm=len(SM)*.25

#print(round(xxvpop))#52 both sides
#print(round(xxvrc))#12 both sides
#print(round(xxvmp))#9
#print(round(xxvmv))#15
#print(round(xxvsm))#15

#Trim at 25%
trimpop=pop[52:-52]
trimrc=RC[12:-12]
trimmp=MP[9:-9]
trimmv=MV[15:-15]
trimsm=SM[15:-15]

#Convert List to Data Frame
v=pd.DataFrame(trimpop).describe()
w=pd.DataFrame(trimrc).describe()
x=pd.DataFrame(trimmp).describe()
y=pd.DataFrame(trimmv).describe()
z=pd.DataFrame(trimsm).describe()

#Summary at 10% Trim
print(f'Population 25%:\n{v}\n\n\
Redwood City 25%:\n{w}\n\n\
Menlo Park 25%:\n{x}\n\n\
Mountain View 25%:\n{y}\n\n\
San Mateo 25%:\n{z}\n\n')
