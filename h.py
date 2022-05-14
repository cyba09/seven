from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import requests
from selenium.common import exceptions
import const
from datetime import datetime, timedelta

bets = const.BETS
idx = 0

def trade(x):
    tabb = driver.find_element(By.CSS_SELECTOR, "div.J5ZZlDCTjcPDVTwQUuf4:nth-child(2) > div:nth-child(2)" )
    driver.execute_script("arguments[0].click();", tabb)
    #WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "odd-item"))).click()
    #tabb.click()
    ammnt = driver.find_element(By.ID,"amount-input")
    ammnt.clear()
    x = str(x)
    for i in x:
        ammnt.send_keys(i)
    
    logn = driver.find_element(By.CLASS_NAME, "place-bet-button")
    driver.execute_script("arguments[0].click();", logn)

def get_results():
    try:
        url = 'https://game3.betgames.tv/s/web/v1/game/results/vegasbets_co_za_ts3?game_id=1&page={page}&date={date}&timezone=2'
        n = datetime.now()
        d = (n - timedelta(days=0)).strftime('%Y-%m-%d')
        p = 1
        res = requests.get(url.format(date=d, page=p)).json()
        arr = [res['runs'][0]['time']]
        for gme in res['runs'][0]['results']:
            arr.append(gme['color'])
        for gme in res['runs'][0]['results']:
            arr.append(gme['number'])
        return arr
    except:
        return ['failed']



    
    
########################################################################################
options = Options()
options.headless = True
options.add_argument('--no-sandbox')
options.add_argument("--start-maximized")
s=Service('/usr/local/bin/chromedriver')
#s=Service('./webdriver/chromedriver.exe')

driver = webdriver.Chrome(service=s, options=options)
url='https://www.vegasbets.co.za/partner/bet-games'
driver.get(url)
try:
    signin = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "qa-Sign in"))
    )
except:
    driver.quit()
signin.click()
#############################print(vegas.getList())
elem = driver.find_element(By.ID, 'qa-username')
#elem = driver.find_element_by_id("UserName")
elem.clear()
elem.send_keys("+27623254346")
passwd = driver.find_element(By.ID, 'qa-password')
#passwd = driver.find_element_by_id("Password")
passwd.clear()
passwd.send_keys("Mpofu@1234")

#btn = driver.find_element_by_css_selector('button.btn.btn-action.btn-block')
btn = driver.find_element(By.ID, 'qa-sign-in-button')
btn.click()
######################################## put EC here
#time.sleep(2)
#betgms = driver.find_element(By.ID, "qa-BETGAMES")
#betgms.click()
time.sleep(21)
driver.switch_to.frame(driver.find_element(By.TAG_NAME,'iframe')) 
#time.sleep(1)
element = driver.find_element(By.CSS_SELECTOR,"button.px2BltBZ9d0JArpfjthg:nth-child(8)")
driver.execute_script("arguments[0].click();", element)
time.sleep(5)
oddeven = driver.find_element(By.CSS_SELECTOR,'button.AKxHERhQ54809pCLD4UV:nth-child(5)')
driver.execute_script("arguments[0].click();", oddeven)
time.sleep(2)
trade(bets[0])

while True:
    curr = datetime.now()
    mnt = curr.minute
    sec = curr.second 
    if (mnt != 0) & (mnt%2 == 0) & (mnt%4 != 0) & (sec == 0) :
        lst = get_results()
        if len(lst) < 2:
            break
        gst = lst[-7:]
        count = 0
        for z in gst:
                if z%2 == 0:
                        count += 1
        if count > 3:
                break
        else:
                idx + 1
        trade(bets[idx])
    time.sleep(1)

time.sleep(10)
driver.close()



