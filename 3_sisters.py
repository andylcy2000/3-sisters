from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import requests


#"ZyP5xwi9xCfFqm83mkESE9uFojZCiRSqsivWVCElqiU"

drivers=[]
for j in range(5):
    drivers.append(webdriver.Chrome('./chromedriver'))


drivers[0].get('https://www.opentix.life/cart/1623860290548998144/1625325104370634753')
drivers[1].get("https://www.opentix.life/cart/1623860290548998144/1625325184191324160")
drivers[2].get("https://www.opentix.life/cart/1623860290548998144/1625021481894866945")
drivers[3].get("https://www.opentix.life/cart/1623860290548998144/1660944117091057665")
drivers[4].get("https://www.opentix.life/cart/1623860290548998144/1625325262265208833")

options = Options()
options.add_argument("--disable-notifications")
count=0
click=True
sum=0
while True:
    for t in range(5):
        drivers[t].refresh()
        unrun=True
        while unrun:
            try:
                sum=0
                element = WebDriverWait(drivers[t], 100).until(
                    EC.presence_of_element_located((By.ID,"l-seating-cart__sidebar--table"))
                )
                #element.click()
                #print("clicked")
                '''
                element2 = WebDriverWait(driver1, 100).until(
                    EC.presence_of_element_located((By.XPATH,"//*[@id=\"l-seating-cart__sidebar--table\"]/div[5]/span[2]"))
                )
                '''
                #print(element2)
                #driver.find_element(By.XPATH,"//*[@id=\"l-seating-cart__sidebar--table\"]/div[5]/span[2]")
                #print("found")
                
                
                soup = BeautifulSoup(drivers[t].page_source, 'html.parser')
                ticket=soup.find_all(class_="section-ticket-remain")
                #print(len(ticket))
                for i in range(4,len(ticket)):
                    if (i!=6 and i!=7):
                        sum+=int(ticket[i].getText()[2:])
                        
                if sum>0:
                    headers = {
                "Authorization": "Bearer " + "", #填入金鑰
                "Content-Type": "application/x-www-form-urlencoded"
            }
        
                    params = {"message": "Ticket found!" }
        
                    r = requests.post("https://notify-api.line.me/api/notify",
                            headers=headers, params=params)
                
                #print("clicked")
                unrun=False
            except:
                pass
    count+=1
    if count>=200:
        headers = {
                "Authorization": "Bearer " + "ZyP5xwi9xCfFqm83mkESE9uFojZCiRSqsivWVCElqiU",
                "Content-Type": "application/x-www-form-urlencoded"
            }
        
        params = {"message": "Already executed two hundred times!" }
        
        r = requests.post("https://notify-api.line.me/api/notify",
                            headers=headers, params=params)
        
        count=0
    #click=False
    #print("did not find")
    #driver.quit()
'''
driver.find_element(By.XPATH,"//*[@id=\"l-seating-cart__sidebar--table\"]")
print("found")
print(s)
print('found')
'''
'''
headers = {
        "Authorization": "Bearer " + "ZyP5xwi9xCfFqm83mkESE9uFojZCiRSqsivWVCElqiU",
        "Content-Type": "application/x-www-form-urlencoded"
    }
 
params = {"message": "Try Try" }
 
r = requests.post("https://notify-api.line.me/api/notify",
                      headers=headers, params=params)
'''







