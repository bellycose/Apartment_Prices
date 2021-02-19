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

#Histogram
plt.hist([dfpop,dfRC,dfMP,dfMV,dfSM],
         12,
         range=(1000,10000),
         ec='k',
         label=['All Cities',
                'Redwood City',
                'Menlo Park',
                'Mountain View',
                'San Mateo'],
         stacked=False)
plt.title("Summary Comparision in Histogram without ASK/$0",
          fontweight='bold',fontsize=16)
plt.xlabel("Price in USD($)",fontweight='bold',fontsize=12)
plt.ylabel("Frequency",fontweight='bold',fontsize=12)
plt.xticks(np.arange(1000,11000,1000))

plt.legend()
plt.show()
