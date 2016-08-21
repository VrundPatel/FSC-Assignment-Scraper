import time
import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#reading the passed username and password in the command line.
parser = argparse.ArgumentParser()
parser.add_argument('username', nargs='+')
parser.add_argument('password', nargs='+')
args = parser.parse_args()

#intializing the Chrome webdriver.
driver = webdriver.Chrome()

#Opening the url for the portal.
driver.get("https://portal.flsouthern.edu/ics")

#Entering the username and password for the user for login.
elem = driver.find_element_by_id("userName")
elem.clear()
elem.send_keys(args.username)
elem = driver.find_element_by_id("password")
elem.clear()
elem.send_keys(args.password)
elem = driver.find_element_by_id("btnLogin")
elem.send_keys(Keys.RETURN)

#Getting the courses for the user.
elem = driver.find_element_by_id("myCourses")
elem.send_keys()
# driver.close()

#writing the assignments to a file.
# with open("assignments.csv", "a") as csv_file:
#     csv_file.write(' '.join())
#     csv_file.close()
