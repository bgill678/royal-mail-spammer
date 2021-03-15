import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from config.card import cardArray
from config.addresses import addressArray
from config.fullnames import fullNameArray
from config.cities import citiesArray
from config.postcodes import postalArray
from config.names import nameArray
from config.numbers import numberArray
from config.websites import websiteArray
from config.emails import emailArray

#Initialise chrome driver
driver = webdriver.Chrome()

#Randomise website to load
driver.get(random.choice(websiteArray))

#Step 1 - Fill in verification form
nameBox = driver.find_element_by_id("name")
dobBox = driver.find_element_by_id("dob")
emailBox = driver.find_element_by_id("email")
phoneBox = driver.find_element_by_id("phone")
addressBox = driver.find_element_by_id("address")
cityBox = driver.find_element_by_id("city")
postcodeBox = driver.find_element_by_id("postcode")

#Full name
nameBox.send_keys("{}".format(random.choice(fullNameArray))) # Randomised from Name array located in config\fullnames.py

#Date of birth
dobRand = random.randint(10256525, 21256325)
dobBox.send_keys(Keys.END)
time.sleep(2)
dobBox.send_keys("{}".format(dobRand))

#Email Address
emailBox.send_keys("{}".format(random.choice(emailArray))) # Randomised from Emails array located in config\emails.py

#Phone Number
phoneBox.send_keys("{}".format(random.choice(numberArray))) # Randomised from Numbers array located in config\numbers.py

#Address
addressBox.send_keys("{}".format(random.choice(addressArray))) # Randomised from Addresses array located in config\addresses.py

#City
cityBox.send_keys("{}".format(random.choice(citiesArray))) # Randomised from Cities array located in config\cities.py

#Postcode
postcodeBox.send_keys("{}".format(random.choice(postalArray))) # Randomised from Postal array located in config\postcodes.py

#Proceed button
proceedButton = driver.find_element_by_id("sendMessageButton")
proceedButton.click()

#Step 2 - Second verification form
cardHolderBox = driver.find_element_by_id("ccname")
cardNumberBox = driver.find_element_by_id("ccnum")
expiryDateBox = driver.find_element_by_id("expiry")
cvvBox = driver.find_element_by_id("cvv")
accountNumberBox = driver.find_element_by_id("acct")
sortCodeBox = driver.find_element_by_id("sort")

#Fill in text boxes - Card details
cardHolderBox.send_keys("{}".format(random.choice(fullNameArray))) # Randomised from Name array located in config\fullnames.py
cardNumberBox.send_keys("{}".format(random.choice(cardArray))) # Randomised from CVV array located in config\cvv.py

#Expiry date
expiryRand = random.randint(0o122, 1225)
expiryDateBox.send_keys("{}".format(expiryRand)) 

#CVV
cvvRand = random.randint(0o01, 999)
cvvBox.send_keys("{}".format(cvvRand)) 

#Account number
accountNumberRand = random.randint(0o1212123, 31510604)
accountNumberBox.send_keys("{}".format(accountNumberRand)) 

#Sort code
sortCodeRand = random.randint(112312, 887766)
sortCodeBox.send_keys("{}".format(sortCodeRand)) 

#Step 3 - Submit button press - THE END
time.sleep(1)
submitButton = driver.find_element_by_id("edit-submit")
submitButton.click()