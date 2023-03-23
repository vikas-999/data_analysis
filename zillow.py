import requests
import pandas as pd
from bs4 import BeautifulSoup
#from collections import Iterable
apt_names = []
apt_address = []
apt_price = []
apt_type = []
apt_link = []
i = 1
while i < 29:

    url=f"https://www.apartments.com/minneapolis-mn/{i}/"
    HEADERS = ({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "Accept-Language": "en-US, en;q=0.5"
    })
    link = requests.get(url, headers=HEADERS)
    #print(link)
    soup = BeautifulSoup(link.text, 'html.parser')
    #print(soup.prettify())
    name = soup.find_all('div', class_='property-title')
    addr = soup.find_all('div', class_='property-address js-url')
    price = soup.find_all('p',class_='property-pricing')
    type = soup.find_all('p',class_='property-beds')
    link = soup.find_all('a',class_='property-link')
    for j in name:
       apt_names.append(j.get_text())
    for k in addr:
        apt_address.append(k.get_text())
    for l in price:
        apt_price.append(l.get_text())
    for m in type:
        apt_type.append(m.get_text())
    for n in link:
        apt_link.append(n['href'])
    
    i+=1

# arranging the dats into rows and columns using pandas

d = pd.DataFrame()
d['apt_names'] = pd.Series(apt_names)
d['apt_address'] = pd.Series(apt_address)
d['apt_price'] = pd.Series(apt_price)
d['apt_type'] = pd.Series(apt_type)
d['apt_link'] = pd.Series(apt_link)

print(d[:25])

#creating an csv file 
#d.to_csv('ZillowApartmens_msp.csv')

#df = pd.read_csv('ZillowApartmens_msp.csv')



    
