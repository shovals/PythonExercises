
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')  # Firefox driver

browser.get('http://ranad.co/vocalzoom/')  # Site location

user = browser.find_element_by_id('txtUser')  # Find the user element on the page by ID
password = browser.find_element_by_id('txtPsw')  # Find the user element on the page by ID

user.send_keys("24")  # In the specific element, send the user value
password.send_keys("24")  # In the specific element, send the user value
elem = browser.find_element_by_id('virtualClockLoginBtn').click()  # Click the correct button

radioselect = browser.find_element_by_id("rdEnterExit_2").click()  # Select the correct radio button selection
project = browser.find_element_by_id("cboProjects")  # Set the drop down as element to use
project.send_keys(Keys.ARROW_DOWN)  # Do down once
project.send_keys(Keys.ARROW_DOWN)  # Do down twice
project.send_keys(Keys.RETURN)  # Select the value and close the drop down element
