import selenium.webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains


driver=webdriver.Chrome(executable_path="C:\\projects\\pythonselenium\\browser\\chromedriver.exe")
driver.maximize_window()

driver.get("https://www.techlistic.com/p/demo-selenium-practice.html")

print(driver.title)

rows= driver.find_elements(By.XPATH, "//*[@id='customers']/tbody/tr")
b=len(rows)
print(b)
cols= driver.find_elements(By.XPATH  ,"//*[@id='customers']/tbody/tr[2]/td")
c=len(cols)
print(c)

for r in range(2 , b+1 ):
    for c in range(1 , c+1):
        options=driver.find_element(By.XPATH, "//*[@id='customers']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(options ,end=' ')
    print()



