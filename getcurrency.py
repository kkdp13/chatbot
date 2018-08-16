#from selenium import webdriver
#from bs4 import BeautifulSoup
#
#
#def getcurrency():
#    chrome_path = r'C:\Users\Tatum\Google Drive\MissRapaportProject\missrapaport\driver\geckodriver.exe'
#    driver = webdriver.Firefox(executable_path=chrome_path)
#    driver.set_page_load_timeout(30)
#    url = 'https://www.superrichthailand.com/#!/en/currency#USD'
#    driver.get(url)
#    soup_level1=BeautifulSoup(driver.page_source, 'lxml')
#    #print(soup_level1.prettify)
#    currency = soup_level1.find('span', {'ng-bind':'currency.sellRate'})
#    #print(currency)
#    newcurrency = currency.text
#    #print(newcurrency)    
#    driver.quit()
#    return newcurrency
#
#ratesuperrich = getcurrency()
#print(ratesuperrich)  

#----------------------------------------------------------------

#import re
import requests
from getnewcurrency import getnewcurrency
#from bs4 import BeautifulSoup

def getcurrency():
    url:str = 'https://www.superrichthailand.com/web/api/v1/rates'
    basic_token:str = 'Basic c3VwZXJyaWNoVGg6aFRoY2lycmVwdXM='

    r = requests.get(url, headers={'Authorization': basic_token})
    r2 = r.text
#match = re.search('curcode"(.*)"', r.text)
#
#strfind1 = '"curcode":"0010"'
#strfind2 = '"cSelling":33.12'
#strfind3 = '"cSelling"'
#strfind4 = '"cBuy1":33.09,'
#print(r.text.find(strfind1))
#print(r.text.find(strfind2))
#print(r.text.find(strfind3))
#print(r.text.find(strfind4))
#print(len(r.text))
#print(r2[275:292])
    currency = r2[284:292]
#    print(currency)
#    currency2 = float(currency)
#    print(currency2)
#    print(type(currency2))
    currency = getnewcurrency(currency)
    return currency

#currency = getcurrency()
#print(currency)
#currency = getcurrency()
#print('the rate from superrich is : {}'.format(currency))
#i = int(r.text.find(strfind1))
#for i in len(r.text):
#    if len(r.text) <= 260
#    print(i)


#if match:
#    print('curcode', match.group(1))
##    print('cSelling', match.group(2))
#else:
#    print('did not find')
#for r in r:
#    print(r)
#soup = BeautifulSoup(r.text, 'lxml')
#currency = soup.find('data', {'exchangeRate':'rate'})
#currency = soup.find('rate')
#print(currency)
#print(soup.text[0])
#{"code":20000,
# "descriptionEn":"Success",
# "description":"ทำรายการเรียบร้อย",
# "data":{"exchangeRate":[{"countryName":"United States",
#                          "cUnit":"USD",
#                          "imgUrl":"https://www.superrichthailand.com:443/assets/images/usd_icon.png",
#                          "rate":[{"cCode":"001",
#                                   "curcode":"0010",
#                                   "cBuying":33.12,
#                                   "cSelling":33.23,
#                                   "cBuy1":33.09,
#                                   "cSell1":33.23,
#                                   "cBuy2":33.07,
#                                   "cSell2":33.23,
#                                   "cBuy3":33,
#                                   "cSell3":null,
#                                   "cBuy4":null,
#                                   "cSell4":null,
#                                   "cBuy5":null,
#                                   "cSell5":null,
#                                   "cBuy6":null,
#                                   "cSell6":null,
#                                   "cBuy7":null,
#                                   "cSell7":null,
#                                   "denom":"100",
#                                   "dateTime":"2018-08-03T21:23:58.983Z",
#                                   "rateDigit":2,"addRate":null},
#                                  {"cCode":"001",
#                                   "curcode":"0011",
#                                   "cBuying":33.12,
#                                   "cSelling":33.23,
#                                   "cBuy1":33.09,
#                                   "cSell1":33.23,
#                                   "cBuy2":33.07,
#                                   "cSell2":33.23,
#                                   "cBuy3":33,
#                                   "cSell3":null,
#                                   "cBuy4":null,
#                                   "cSell4":null,
#                                   "cBuy5":null,
#                                   "cSell5":null,
#                                   "cBuy6":null,
#                                   "cSell6":null,
#                                   "cBuy7":null,
#                                   "cSell7":null,
#                                   "denom":"50",
#                                   "dateTime":"2018-08-03T21:23:58.983Z",
#                                   "rateDigit":2,
#                                   "addRate":null},
#                                  {"cCode":"001",
#                                   "curcode":"0012",
#                                   "cBuying":32.97,
#                                   "cSelling":33.13,
#                                   "cBuy1":32.92,
#                                   "cSell1":33.13,
#                                   "cBuy2":32.87,
#                                   "cSell2":33.13,
#                                   "cBuy3":32.62,
#                                   "cSell3":null,
#                                   "cBuy4":null,
#                                   "cSell4":null,
#                                   "cBuy5":null,
#                                   "cSell5":null,
#                                   "cBuy6":null,
#                                   "cSell6":null,
#                                   "cBuy7":null,
#                                   "cSell7":null,
#                                   "denom":"10 - 20",
#                                   "dateTime":"2018-08-03T21:23:58.983Z",
#                                   "rateDigit":2,
#                                   "addRate":null},
#                                  {"cCode":"001",
#                                   "curcode":"0013",
#                                   "cBuying":32.87,
#                                   "cSelling":33.13,
#                                   "cBuy1":32.82,
#                                   "cSell1":33.13,
#                                   "cBuy2":32.77,
#                                   "cSell2":33.13,
#                                   "cBuy3":32.62,
#                                   "cSell3":null,
#                                   "cBuy4":null,
#                                   "cSell4":null,
#                                   "cBuy5":null,
#                                   "cSell5":null,
#                                   "cBuy6":null,
#                                   "cSell6":null,
#                                   "cBuy7":null,
#                                   "cSell7":null,
#                                   "denom":"5",
#                                   "dateTime":"2018-08-03T21:23:58.983Z",
#                                   "rateDigit":2,
#                                   "addRate":null},
#                                  {"cCode":"001",
#                                   "curcode":"0014",
#                                   "cBuying":32.52,
#                                   "cSelling":32.93,
#                                   "cBuy1":32.44,
#                                   "cSell1":32.93,
#                                   "cBuy2":32.42,
#                                   "cSell2":32.93,
#                                   "cBuy3"                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   
                                   