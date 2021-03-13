import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from config import monthArray
from config import countyArray

#Chrome driver
driver = webdriver.Chrome()
driver.get("https://royalmail-parcel-tracking.com/register.php")

#ID selections
submitButton = driver.find_element_by_id("edit-submit")
phoneBox = driver.find_element_by_id("phone")

# Step 1 - Send phone number
phoneBox.send_keys("01234567890") # RANDOMISE
submitButton.click()

#Sleep (3 seconds) to allow proceed button to show
time.sleep(3)
proceedButton = driver.find_element_by_id("proceed")
proceedButton.click()

#Sleep (2 seconds) to allow loading
time.sleep(2)

#Step 2 - Fill in verification form
nameBox = driver.find_element_by_id("fname")
dobBoxDD = driver.find_element_by_id("day")
dobBoxMM = Select(driver.find_element_by_css_selector('#month'))
dobBoxYY = driver.find_element_by_id("year")
addressBox = driver.find_element_by_id("address")
cityBox = driver.find_element_by_id("city")
countyBox = Select(driver.find_element_by_name('county'))
postcodeBox = driver.find_element_by_id("postcode")
memorableNameBox = driver.find_element_by_id("mmn")

#Use month array
dobBoxMM.select_by_visible_text(random.choice(monthArray))

#Use county array
countyBox.select_by_visible_text(random.choice(countyArray))

#Fill in text boxes - Personal info
nameBox.send_keys("John Doe") # RANDOMISE
dobBoxDD.send_keys("12") # RANDOMISE
dobBoxYY.send_keys("1998") # RANDOMISE
addressBox.send_keys("12 john avenue, stephen row") # RANDOMISE
cityBox.send_keys("London") # RANDOMISE
postcodeBox.send_keys("NW12") # RANDOMISE
memorableNameBox.send_keys("Johnathan") # RANDOMISE

#Submit button press
time.sleep(1)
submitButton = driver.find_element_by_id("edit-submit")
submitButton.click()

#Step 4 - Second verification form
cardHolderBox = driver.find_element_by_id("ccname")
cardNumberBox = driver.find_element_by_id("ccnum")
expiryDateBox = driver.find_element_by_id("expiry")
cvvBox = driver.find_element_by_id("cvv")
accountNumberBox = driver.find_element_by_id("acct")
sortCodeBox = driver.find_element_by_id("sort")

#Fill in text boxes - Card details
cardHolderBox.send_keys("John Doe") # RANDOMISE
cardNumberBox.send_keys("5532 6656 9966 6406") # RANDOMISE
expiryDateBox.send_keys("05/2025") # RANDOMISE
cvvBox.send_keys("123") # RANDOMISE
accountNumberBox.send_keys("225568") # RANDOMISE
sortCodeBox.send_keys("532515") # RANDOMISE