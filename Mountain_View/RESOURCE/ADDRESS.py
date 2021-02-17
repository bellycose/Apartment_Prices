from bs4 import BeautifulSoup as bs
import requests
from time import sleep

s=requests.Session()
def address():
    baseURL='https://www.apartmentlist.com/ca/mountain-view'
    r=s.get(baseURL)
    soup=bs(r.content,'html.parser')

    block=soup.find_all('div',class_='css-1ffl9o8 ekhz9bg3')
    sleep(1)
        
    address=[]
    for properties in block:
        addressBlock=properties.find('div',class_='css-1484omx e131nafx0').text
        address.append(addressBlock)    
    return address
    #print(address)


address()
