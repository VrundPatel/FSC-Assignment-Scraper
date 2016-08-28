import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Reading credentials from the text file
file = open("credentials.txt", 'r')
username = file.readline()
password = file.readline()

# Intializing the Chrome webdriver.
driver = webdriver.Chrome()

# Initializing the actions driver.
actions = ActionChains(driver)

# Opening the url for the portal.
driver.get("https://portal.flsouthern.edu/ICS/Students/")

#Entering the username and password for the user for login.
elem = driver.find_element_by_id("userName")
elem.clear()
elem.send_keys(username)
elem = driver.find_element_by_id("password")
elem.clear()
elem.send_keys(password)
elem = driver.find_element_by_id("btnLogin")
elem.send_keys(Keys.RETURN)

# course = driver.find_element_by_id("pg1_V_rptrCourses_ctl01_rptrItems_ctl01_hlCourseCode")
# print("found course")
# actions.click(course)
driver.get("https://portal.flsouthern.edu/ICS/Academics/REL/REL__1108/2016_DF-REL__1108-003/")
driver.get("https://portal.flsouthern.edu/ICS/Academics/REL/REL__1108/2016_DF-REL__1108-003/Coursework.jnz")
#Getting the courses for the user.
# elem = driver.find_element_by_id("myCourses")
# elem.send_keys()
# driver.close()

# changes the assignmnet number in the list and prints the text of it. 
for i in range(100, 105):
    driver.find_element_by_class_name("assignmentText")
    id = "pg0_V__assignmentView__rptAssignments_ctl00__studentAssignBody__rptAssignments_ct" + str(i) + "__hyAssign"
    elem = driver.find_elements_by_id(id)
    print(elem.text)

#   writing the assignments to a file.
# with open("assignments.csv", "a") as csv_file:
#     csv_file.write(' '.join())
#     csv_file.close()
