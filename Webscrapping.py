from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import os
import sys
now = datetime.now()
dt = now.strftime("%m%d%y")

option = Options()
option.headless = True
driver_service = Service(executable_path='chromedriver_win32')
driver = webdriver.Chrome(service=driver_service,options=option)
driver.get('https://www.thesun.co.uk/sport/football/')
t = []
s = []
l = []
containers = driver.find_elements(By.XPATH, value= '//div[@class="teaser__copy-container"]')
for container in containers:
    title = container.find_element(By.XPATH, value='./a/h3').text
    subtitle = container.find_element(By.XPATH, value='./a/p').text
    link = container.find_element(By.XPATH, value='./a').get_attribute('href')
    t.append(title)
    s.append(subtitle)
    l.append(link)

d = {'Title': t, 'Subtile': s, 'Link': l}
df = pd.DataFrame(d)
filename = f'news_{dt}.csv'
#final_path = os.path.join(application_name, filename)
df.to_csv(filename)
driver.quit()
