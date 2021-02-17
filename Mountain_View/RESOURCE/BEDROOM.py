from bs4 import BeautifulSoup as bs
import requests
from time import sleep
from random import randint

s=requests.Session()
def bedroom():
    baseURL='https://www.apartmentlist.com/ca/mountain-view'
    r=s.get(baseURL)
    soup=bs(r.content,'html.parser')

    block=soup.find_all('div',class_='css-1u6cvl9 e1k7pw6k0')
    sleep(randint(2,10))

    result=[]
    for properties in block:
        bedroomBlock=properties.find_all('div',class_='css-10a5kw e131nafx0')
        bedroom=[bedroom.text for bedroom in bedroomBlock]
        result+=[insert for insert in bedroom ]
    return result
    #print(result)

            
bedroom()


