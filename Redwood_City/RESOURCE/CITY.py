from bs4 import BeautifulSoup as bs
import requests
from time import sleep

s=requests.Session()
def city():
    baseURL='https://www.apartmentlist.com/ca/redwood-city'
    r=s.get(baseURL)
    soup=bs(r.content,'html.parser')

    block=soup.find_all('div',class_='css-1u6cvl9 e1k7pw6k0')
    sleep(1)
        
    city=[]
    for properties in block:
        try:
            cityguess=properties.find_next_sibling('div',class_='css-1484omx e131nafx0').text
        except:
            cityguess='Redwood City'
        city.append(cityguess)
    return city
    #print(city)

city()
