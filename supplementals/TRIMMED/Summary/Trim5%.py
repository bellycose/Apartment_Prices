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
#print(len(pop))#207-20
#print(len(RC))#50-4
#print(len(MP))#36-4
#print(len(MV))#60-6
#print(len(SM))#61-6

#Calculate for 5% Trimming
vpop=len(pop)*.05
vrc=len(RC)*.05
vmp=len(MP)*.05
vmv=len(MV)*.05
vsm=len(SM)*.05

#print(round(vpop))#10 both sides
#print(round(vrc))#2
#print(round(vmp))#2
#print(round(vmv))#3
#print(round(vsm))#3

#Trimming at 5%
'''
Test:
leftpop=pop[:10]#10
rightpop=pop[-10:]#10
trimpop=pop[10:-10]
print(trimpop)
'''
trimpop=pop[10:-10]
trimrc=RC[2:-2]
trimmp=MP[2:-2]
trimmv=MV[3:-3]
trimsm=SM[3:-3]

#Trimmed Length
#print(len(trimpop))
#print(len(trimrc))
#print(len(trimmp))
#print(len(trimmv))
#print(len(trimsm))

#Convert List to Data Frame
v=pd.DataFrame(trimpop).describe()
w=pd.DataFrame(trimrc).describe()
x=pd.DataFrame(trimmp).describe()
y=pd.DataFrame(trimmv).describe()
z=pd.DataFrame(trimsm).describe()

#Summary at 10% Trim
print(f'Population 5%:\n{v}\n\n\
Redwood City 5%:\n{w}\n\n\
Menlo Park 5%:\n{x}\n\n\
Mountain View 5%:\n{y}\n\n\
San Mateo 5%:\n{z}\n\n')
