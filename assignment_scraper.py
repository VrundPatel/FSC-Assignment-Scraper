from __future__ import print_function
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# Reading credentials from the text file
file = open("credentials.txt", 'r')
outputFile = open("assignments.txt", 'w')
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

# Words to be eliminated from the assignmnet due text.
eliminate_words = ["Homework due", "Exam due", "Paper due", "Participation due", "(Required)", "(Optional)"]

# Looping through the list of courses.
for i in range(1, 5):
    # finds the name for each course
    course_name = driver.find_element_by_id("pg1_V_rptrCourses_ctl01_rptrItems_ctl0" +  str(i) + "_hlCourseCode").text
    # finds the link for each course and goes to the section
    driver.find_element_by_id("pg1_V_rptrCourses_ctl01_rptrItems_ctl0" +  str(i) + "_hlCourseCode").click()
    # clicks on the couse work link where all the assignments are listed.
    driver.find_element_by_link_text('Coursework').click()

    # Gets the main display where the assignmnets are displayed.
    assignmentsDisplay = driver.find_elements_by_class_name("assignmentDisplay")

    # will hold list of assignments
    assignments = []

    # Going through the main display and find each div with the assignment text
    # and the due date for each assignment and add it to the array.
    for assignment in assignmentsDisplay:
        assignments.append(assignment.find_element_by_class_name("assignmentText").text)
        text = assignment.find_element_by_class_name("assignmentDue").text
        # deletes the eliminated words
        for word in eliminate_words:
            if word in text:
                text = text.replace(word, "")
        assignments.append(text.strip())
        assignments.append("")

    # Prints the text to an output file if there are any assignments available for the class.
    if assignments:
        print("------------" + course_name + "--------------", file=outputFile)
        # Prints the text of the list to an output file.
        for assignment in assignments:
            print(assignment, file=outputFile)

    # Redirecting to the main page.
    driver.get("https://portal.flsouthern.edu/ICS/Students/")

#   writing the assignments to a file.
# with open("assignmentsCal.csv", "a") as csv_file:
#     csv_file.write(' '.join())
#     csv_file.close()

# closes the browser
driver.close()
