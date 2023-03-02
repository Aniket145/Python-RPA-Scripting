from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver =webdriver.Chrome()
import csv
import time
import pandas as pd
url="https://www.cleartrip.com/"
driver.get(url)
driver.maximize_window()

source=driver.find_element(By.XPATH,value='//*[@id="root"]/div/div/div[1]/div/div[2]/div/div[1]/div/div[3]/div[3]/div/div/div[1]/input')
source.send_keys("Bangalore")
time.sleep(5)
click_on_scource=driver.find_element(By.XPATH,value='//*[@id="root"]/div/div/div[1]/div/div[2]/div/div[1]/div/div[3]/div[3]/div/div[1]/div[1]/div[2]/ul/li/div/div[2]/p').click()
time.sleep(5)

destination=driver.find_element(By.XPATH,value='/html/body/div/div/div/div[1]/div/div[2]/div/div[1]/div/div[3]/div[3]/div/div/div[3]/input')
destination.send_keys("Delhi")
time.sleep(5)
click_on_destination=driver.find_element(By.XPATH,value='//*[@id="root"]/div/div/div[1]/div/div[2]/div/div[1]/div/div[3]/div[3]/div/div[1]/div[3]/div[2]/ul/li/div/div[2]/p').click()
time.sleep(5)

click_on_search=driver.find_element(By.XPATH,value='/html/body/div/div/div/div[1]/div/div[2]/div/div[1]/div/div[3]/div[4]/div/div[2]/span').click()
time.sleep(10)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(5)

flight_name = driver.find_elements(By.XPATH, '//div[@class="flex flex-column flex-start"]')
flight_list = []
for fn in flight_name:
    text_element = fn.find_element(By.XPATH, './/p[@class="fw-500 fs-2 c-neutral-900"]')
    text = text_element.text
    flight_list.append(text)

price = driver.find_elements(By.XPATH, '//div[@class="flex flex-column flex-center flex-right p-relative"]')
flight_price = []
for fp in price:
    text_element = fp.find_element(By.XPATH, './/p[@class="m-0 fs-5 fw-700 c-neutral-900 false"]')
    text = text_element.text.replace("₹","Rs.")
    flight_price.append(text)

df=pd.DataFrame({"Flight Name":flight_list,"Flight Price":flight_price})
print(df)
df.to_csv("Excel_flight3.csv")

df = pd.read_csv('Excel_flight3.csv')
smallest_row = df.loc[df['Flight Price'] == df['Flight Price'].min()]
cheapest_price = smallest_row['Flight Price'].iloc[0]
cheapest_flight = smallest_row['Flight Name'].iloc[0]

print(f"The cheapest flight price is {cheapest_price} and cheapest flight name is {cheapest_flight}.")
