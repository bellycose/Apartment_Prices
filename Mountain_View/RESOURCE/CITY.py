from bs4 import BeautifulSoup as bs
import requests
from time import sleep
from random import randint

s=requests.Session()
def city():
    baseURL='https://www.apartmentlist.com/ca/mountain-view'
    r=s.get(baseURL)
    soup=bs(r.content,'html.parser')

    block=soup.find_all('div',class_='css-1u6cvl9 e1k7pw6k0')
    sleep(randint(2,10))
        
    city=[]
    for properties in block:
        try:
            cityguess=properties.find_next_sibling('div',class_='css-1484omx e131nafx0').text
        except:
            cityguess='Moutain View'
        city.append(cityguess)
    return city
    #print(city)


city()
