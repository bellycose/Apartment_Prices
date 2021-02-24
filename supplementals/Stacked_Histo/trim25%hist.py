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

#Trim at 25%
trimpop=pop[52:-52]
trimrc=RC[12:-12]
trimmp=MP[9:-9]
trimmv=MV[15:-15]
trimsm=SM[15:-15]

#Histogram
plt.hist([trimrc,trimmp,trimmv,trimsm],
         10,
         range=(1500,4000),
         ec='k',
         label=['Redwood City',
                'Menlo Park',
                'Mountain View',
                'San Mateo'],
         color=['orange','limegreen','crimson','mediumpurple'],
         align='left',
         stacked=True)
plt.title("Summary Comparision in Histogram\nTrimmed 25%",
          fontweight='bold',fontsize=16)
plt.xlabel("Price in USD($)",fontweight='bold',fontsize=12)
plt.ylabel("Frequency",fontweight='bold',fontsize=12)
plt.xticks(np.arange(1500,4000,250))

plt.legend()
plt.show()
