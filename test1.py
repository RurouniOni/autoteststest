from selenium import webdriver

driver_location = "/snap/bin/chromium"
binary_location = "/usr/bin/chromium-browser"

options = webdriver.ChromeOptions()
options.binary_location = binary_location
driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com")
print(driver.page_sourceencode('utf8'))
driver.quit()