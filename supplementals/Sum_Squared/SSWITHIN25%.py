import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import statistics

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

#Total Sum of Square
#Population
frame=[bdrc,bdmp,bdmv,bdsm]
result=pd.concat(frame)
popPrices=result["Price"]
pop=sorted(popPrices)
trimpop=pop[52:-52]

#Grand Mean
xpop=sum(trimpop)/len(trimpop) #Cannot use trimpop.mean() due to Error Attr.
print(xpop) #2678.76

#Sum of Square Total
ss=[math.pow(popsq-xpop,2) for popsq in trimpop]
print(sum(ss)) #14601392.93

#Sum of Square Within
bdrcPrice=bdrc['Price']
bdmpPrice=bdmp['Price']
bdmvPrice=bdmv['Price']
bdsmPrice=bdsm['Price']

#Sorted in Order
RC=sorted(bdrcPrice)
MP=sorted(bdmpPrice)
MV=sorted(bdmvPrice)
SM=sorted(bdsmPrice)

#Trimming at 5%
trimrc=RC[12:-12]
trimmp=MP[9:-9]
trimmv=MV[15:-15]
trimsm=SM[15:-15]

#Cities Mean Square
xrc=sum(trimrc)/len(trimrc)
xmp=sum(trimmp)/len(trimmp)
xmv=sum(trimmv)/len(trimmv)
xsm=sum(trimsm)/len(trimsm)
ssrc=[math.pow(poprc-xrc,2) for poprc in trimrc]
ssmp=[math.pow(popmp-xmp,2) for popmp in trimmp]
ssmv=[math.pow(popmv-xmv,2) for popmv in trimmv]
sssm=[math.pow(popsm-xsm,2) for popsm in trimsm]

print(sum(ssrc))#3582756.46
print(sum(ssmp))#5501637.61
print(sum(ssmv))#3071955.37
print(sum(sssm))#4264498.19
