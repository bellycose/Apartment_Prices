from bs4 import BeautifulSoup as bs
import requests
import re
from time import sleep
from random import randint

s=requests.Session()
def price():
    baseURL='https://www.apartmentlist.com/ca/mountain-view'
    r=s.get(baseURL)
    soup=bs(r.content,'html.parser')

    block=soup.find_all('div',class_='css-1ffl9o8 ekhz9bg3')
    sleep(randint(2,10))

    result=[]
    for properties in block:
        priceBlock=properties.find_all('div',class_="css-q23zey e131nafx0")
        price=[price.text for price in priceBlock]
        strPrice=''.join(price) #Change from list to string type
        removed=r'[$]' #Select and remove $ characters
        removed2=r'Ask' #Select and remove Ask
        removed3=r'[,]' #Select and remove comma
        modPrice=re.sub(removed,' ',strPrice)#Substitute $ for '_'
        modPrice2=re.sub(removed2,' 0',modPrice)#Substitute Ask for _0
        modPrice3=re.sub(removed3,'',modPrice2)#Eliminate space within price
        segments=modPrice3.split()#Change string with updates into list, remain clusted
        
        result+=[insert for insert in segments]
    return result
    #print(result)
            

price()
