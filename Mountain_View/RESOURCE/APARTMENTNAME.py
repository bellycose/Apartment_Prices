from bs4 import BeautifulSoup as bs
import requests
from time import sleep

s=requests.Session() #Establish a TCP without having to reestablish connection
def apartmentName():
    baseURL='https://www.apartmentlist.com/ca/mountain-view'
    r=s.get(baseURL)
    soup=bs(r.content,'html.parser')

    block=soup.find_all('div',class_='css-1ffl9o8 ekhz9bg3')
    sleep(1)

    apartment=[]
    for properties in block:
        apartmentBlock=properties.find('a').text
        apartment.append(apartmentBlock)
    return apartment
    #print(apartment)   


apartmentName()
