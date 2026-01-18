from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

try:
    driver.get("https://www.google.com")
    sleep(2)
    search_box = driver.find_element(By.NAME, "q") #def name for google searching
    search_box.send_keys("Python Selenium") # print text
    sleep(2)
    search_box.send_keys(Keys.ENTER)
    sleep(2)
    #site_1 = driver.find_element(By.XPATH, value="//*[contains(text(),'Python Selenium')]")
    sleep(2)
    print(f"URL: {driver.current_url}")
    print(f"Page_title: {driver.title}")

except Exception as e:
    print(f"Error: {e}")

finally:
    driver.quit()