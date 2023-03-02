import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

website = "https://web.whatsapp.com/"
phone = "+919692612030"
message = "Test"
path = 'chromedriver_win32/chromedriver.exe'
options = Options()
options.add_experimental_option("debuggerAddress", "localhost:8989")
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
driver.get(website)
time.sleep(45)
