import requests
from bs4 import BeautifulSoup
import sys

# you can change the keyword in the place of samsung j7

keyword = "samsung j7"







def amazon(x):
    # t = []
    #select a particular url 
    url = ("https://www.amazon.in/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=")
    #replace command help to replace letters  
    x = x.replace(" ","+")                                                                     
    print(url+str(x))      
    #extract the data from a webiste by using BeautifulSoup                                                                    
    soup = BeautifulSoup(requests.get(url+str(x)).text, "html.parser")                        
    #print(soup)
    #the below varliable will help you to find the internal link
    ahref = str(soup.find("div",{"class": "a-row a-spacing-none"}).find("a")['href'])            
    print(ahref)
    #requests get href will extract the data from the internal links
    r = requests.get(ahref)
    soup = BeautifulSoup(r.content, "html.parser")                                                                #requests.get(ahref) is to get text from internal links                                                                         
    #price = soup.find("td",{"class": "a-span12"})
    # to find out the price for an particular product 
    price = soup.find("span",{"class": "a-size-medium a-color-price"}).text.strip()
    print(price)
    



def filpkart(x):
    url = ("https://www.flipkart.com/search?q=")
    x = x.replace(" ","+")    
    print(url+str(x)) 
    soup = BeautifulSoup(requests.get(url+str(x)).text, "html.parser")
    links = str("https://www.flipkart.com")+str(soup.find("a",{"rel": "noopener noreferrer"})["href"])
    print(links)
    r = requests.get(links)
    soup = BeautifulSoup(r.text, "html.parser")
    price = soup.find("div", {"class": "_3qQ9m1"}).text
    print(price)
    

def snapdeal(x):
    url = ("https://www.snapdeal.com/search?keyword=")
    x = x.replace(" ", "+")
    print(url+str(x))
    soup = BeautifulSoup(requests.get(url+str(x)).text, "html.parser")
    ahref = str(soup.find("div",{"data-js-pos": "0"}).find("a")["href"])
    # print(ahref.find("a")["href"])
    # r = requests.get((ahref.find("a")["href"]))
    # soup = BeautifulSoup(r.text, "html.parser")
    # price = soup.find("span", {"class": "payBlkBig"})
    # print(price.text)
    print(ahref)
    r = requests.get(ahref)
    soup = BeautifulSoup(r.text, "html.parser")
    price = soup.find("span", {"class": "payBlkBig"})
    print(price.text)








amazon(keyword)
filpkart(keyword)
snapdeal(keyword)

sys.exit()
