from bs4 import BeautifulSoup as bs
import requests
from time import sleep

s=requests.Session()
def city():
    baseURL='https://www.apartmentlist.com/ca/menlo-park'
    r=s.get(baseURL)
    soup=bs(r.content,'html.parser')

    block=soup.find_all('div',class_='css-hpgf8j emzreiv0')
    sleep(1)
        
    city=[]
    for properties in block:
        try:
            cityguess=properties.find_next_sibling('div',class_='css-1484omx e131nafx0').text
        except:
            cityguess='Menlo Park'
        city.append(cityguess)
    return city
    #print(city)


city()
