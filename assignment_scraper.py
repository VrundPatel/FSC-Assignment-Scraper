import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://portal.flsouthern.edu/ics")
elem = driver.find_element_by_id("userName")
elem.clear()
elem.send_keys("userName")
elem = driver.find_element_by_id("password")
elem.clear()
elem.send_keys("password")
elem = driver.find_element_by_id("btnLogin")
elem.send_keys(Keys.RETURN)
elem = driver.find_element_by_id("myCourses")
elem.send_keys()
# driver.close()
