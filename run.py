import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from config.arrays import monthArray
from config.arrays import countyArray
from config.card import cardArray
from config.addresses import addressArray
from config.fullnames import fullNameArray
from config.cities import citiesArray
from config.postcodes import postalArray
from config.names import nameArray
from config.numbers import numberArray

#Chrome driver
driver = webdriver.Chrome()
driver.get("https://royalmail-parcel-tracking.com/register.php")

#ID selections
submitButton = driver.find_element_by_id("edit-submit")
phoneBox = driver.find_element_by_id("phone")

# Step 1 - Send phone number
phoneBox.send_keys("{}".format(random.choice(numberArray))) # Randomised from Number array located in config\numbers.py
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

#Fill in text boxes - Personal info
dobBoxMM.select_by_visible_text(random.choice(monthArray)) # Randomised from Month array located in config\arrays.py

countyBox.select_by_visible_text(random.choice(countyArray)) # Randomised from County array located in config\arrays.py

nameBox.send_keys("{}".format(random.choice(fullNameArray))) # Randomised from Name array located in config\fullnames.py

dayRand = random.randint(1, 30)
dobBoxDD.send_keys("{}".format(dayRand)) 

yearRand = random.randint(1958, 2002)
dobBoxYY.send_keys("{}".format(yearRand))

addressBox.send_keys("{}".format(random.choice(addressArray))) # Randomised from Address array located in config\addresses.py

cityBox.send_keys("{}".format(random.choice(citiesArray))) # Randomised from Cities array located in config\cities.py

postcodeBox.send_keys("{}".format(random.choice(postalArray))) # Randomised from Postal array located in config\postcodes.py

memorableNameBox.send_keys("{}".format(random.choice(nameArray))) # Randomised from Names array located in config\names.py

#Submit button press - Personal info
time.sleep(1)
submitButton = driver.find_element_by_id("edit-submit")
submitButton.click()

#Step 3 - Second verification form
cardHolderBox = driver.find_element_by_id("ccname")
cardNumberBox = driver.find_element_by_id("ccnum")
expiryDateBox = driver.find_element_by_id("expiry")
cvvBox = driver.find_element_by_id("cvv")
accountNumberBox = driver.find_element_by_id("acct")
sortCodeBox = driver.find_element_by_id("sort")

#Fill in text boxes - Card details
cardHolderBox.send_keys("{}".format(random.choice(fullNameArray))) # Randomised from Name array located in config\fullnames.py
cardNumberBox.send_keys("{}".format(random.choice(cardArray))) # Randomised from CVV array located in config\cvv.py

expiryRand = random.randint(0o122, 1225)
expiryDateBox.send_keys("{}".format(expiryRand)) 

cvvRand = random.randint(0o01, 999)
cvvBox.send_keys("{}".format(cvvRand)) 

accountNumberRand = random.randint(0o1212123, 31510604)
accountNumberBox.send_keys("{}".format(accountNumberRand)) 

sortCodeRand = random.randint(112312, 887766)
sortCodeBox.send_keys("{}".format(sortCodeRand)) 

#Step 4 - Submit button press - THE END
time.sleep(1)
submitButton = driver.find_element_by_id("edit-submit")
submitButton.click()