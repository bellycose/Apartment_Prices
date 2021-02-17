from bs4 import BeautifulSoup as bs
import requests
from time import sleep

s=requests.Session()
def address():
    baseURL='https://www.apartmentlist.com/ca/menlo-park'
    r=s.get(baseURL)
    soup=bs(r.content,'html.parser')

    block=soup.find_all('div',class_='css-hpgf8j emzreiv0')
    sleep(1)
        
    address=[]
    for properties in block:
        addressBlock=properties.find('div',class_='css-1484omx e131nafx0').text
        address.append(addressBlock)    
    return address


address()
