#https://data.census.gov/cedsci/table?g=0400000US06_1600000US0646870,0649670,0660102,0668252&tid=ACSDP5Y2019.DP04&hidePreview=false

menloparkpop=11906 #Total housing occupancy 2019
menloparkrent=5010 #Total renters 2019
percentageMP=(menloparkrent/menloparkpop)*100

mountainviewpop=33756
mountainviewrent=19700
percentageMV=(mountainviewrent/mountainviewpop)*100

redwoodcitypop=30829
redwoodcityrent=15487
percentageRC=(redwoodcityrent/redwoodcitypop)*100

sanmateopop=38549
sanmateorent=17570
percentageSM=(sanmateorent/sanmateopop)*100

print(f'Menlo Park\nTotal Pop: 11906\nRental Occupancy(%):{percentageMP:.2f}%\n\n\
Mountain View\nTotal Pop: 33756\nRental Occupancy(%):{percentageMV:.2f}%\n\n\
Redwood City\nTotal Pop: 30829\nRental Occupancy(%):{percentageRC:.2f}%\n\n\
San Mateo\nTotal Pop: 38549\nRental Occupancy(%):{percentageSM:.2f}%\n\n')

#Output
'''
Menlo Park
Total Pop: 11906
Rental Occupancy(%):42.08%

Mountain View
Total Pop: 33756
Rental Occupancy(%):58.36%

Redwood City
Total Pop: 30829
Rental Occupancy(%):50.24%

San Mateo
Total Pop: 38549
Rental Occupancy(%):45.58%
'''
#Rental Occupancy includes property owners and tenants for LTR and STR.
