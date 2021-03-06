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
#print(dfpop)
#print(dfRC)
#print(dfMP)
#print(dfMV)
#print(dfSM)

#Boxplot
fig1,ax1,ax2,ax3,ax4,ax5=plt.boxplot([dfpop,dfRC,dfMP,dfMV,dfSM],
                                     labels=['All',
                                             'Redwood City',
                                             'Menlo Park',
                                             'Mountain View',
                                             'San Mateo'],
                                     vert=True,
                                     showmeans=True,
                                     sym='b.',
                                     showfliers=True,
                                     autorange=False,)

plt.ylabel("Price in USD($)\n",
           fontweight='bold',
           fontsize=12,
           )
plt.title("Summary of Prices in Each Cities",
          fontweight='bold',
          fontsize=16)

plt.show()
