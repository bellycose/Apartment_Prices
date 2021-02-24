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

#Grand Mean
xpop=popPrices.mean()
#print(xpop) #2601.07

#Sum of Square Total
ss=[math.pow(popsq-xpop,2) for popsq in popPrices]
#print(sum(ss)) #472349857.91


#Sum of Square Within
bdrcPrice=bdrc['Price']
bdmpPrice=bdmp['Price']
bdmvPrice=bdmv['Price']
bdsmPrice=bdsm['Price']
#Cities Mean Square
xrc=bdrcPrice.mean()
xmp=bdmpPrice.mean()
xmv=bdmvPrice.mean()
xsm=bdsmPrice.mean()
ssrc=[math.pow(poprc-xrc,2) for poprc in bdrcPrice]
ssmp=[math.pow(popmp-xmp,2) for popmp in bdmpPrice]
ssmv=[math.pow(popmv-xmv,2) for popmv in bdmvPrice]
sssm=[math.pow(popsm-xsm,2) for popsm in bdsmPrice]

print(sum(ssrc))#76228484.82
print(sum(ssmp))#166049835.64
print(sum(ssmv))#90451628.18
print(sum(sssm))#121274272.85
