from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
import csv
import re

Name = []
Price = []


driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("ipads")
search_box.send_keys(Keys.RETURN)
time.sleep(5)
num_pages = int(driver.find_element(By.CSS_SELECTOR, "div._2MImiq span").text.split()[-1])
for page in range(num_pages):
    ipad_products = driver.find_elements(By.CSS_SELECTOR, "div._2kHMtA")
    for product in ipad_products:
        name = product.find_element(By.CSS_SELECTOR, "div._4rR01T").text
        price = product.find_element(By.CSS_SELECTOR, "div._30jeq3._1_WHN1").text
        Name.append(name)
        Price.append(price)
        # print(name, "-", price)

    next_button = driver.find_element(By.CSS_SELECTOR, "a._1LKTO3")
    driver.execute_script("arguments[0].click();", next_button)

    time.sleep(5)

d = {'Name': Name, 'Price': Price}
df = pd.DataFrame(d)
filename = f'IPAD.csv'
df.to_csv(filename)
driver.quit()
#printing ipads with 128 ROM version
with open('IPAD.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        for item in row:
            if re.search(r'\b128\b', item):
                print(row)
                break
