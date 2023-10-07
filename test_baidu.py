from selenium import webdriver

# chromedriver = r"D:\drivers\chromedriver.exe"
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

driver.find_element_by_id("kw").send_keys("Selenium")
driver.find_element_by_id("su").click()

# driver.quit()
