from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
import requests

driver = webdriver.Chrome()

driver.get("https://automationexercise.com/")

print("..Halaman akan ditampilkan dalam 5 detik..")
time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[4]/a').click()
time.sleep(3)


username = "testerAA"
email = "testerAAA@mail.com"

username_field = driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/input[2]')
email_field = driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/input[3]')

username_field.send_keys(username)
email_field.send_keys(email)

driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/button').click()
time.sleep(5)

driver.find_element(By.ID, 'id_gender1').click()
time.sleep(2)
title_selected = "Mr"

driver.find_element(By.ID, "password").send_keys("P@ssw0rd")
time.sleep(2)
driver.find_element(By.ID, "days").send_keys("17")
time.sleep(2)
driver.find_element(By.ID, "months").send_keys("March")
time.sleep(2)
driver.find_element(By.ID, "years").send_keys("1990")
time.sleep(2)

driver.find_element(By.ID, "newsletter").click()
driver.find_element(By.ID, "optin").click()

driver.find_element(By.ID, "first_name").send_keys("John")
driver.find_element(By.ID, "last_name").send_keys("Doe")
driver.find_element(By.ID, "company").send_keys("Dream Company")
driver.find_element(By.ID, "address1").send_keys("Sky Street")
driver.find_element(By.ID, "address2").send_keys("No 12")
time.sleep(2)

country_dropdown = Select(driver.find_element(By.ID, "country"))
country_dropdown.select_by_visible_text("Singapore")
selected_country = country_dropdown.first_selected_option.text
time.sleep(2)

driver.find_element(By.ID, "state").send_keys("xxx")
driver.find_element(By.ID, "city").send_keys("zzz")
driver.find_element(By.ID, "zipcode").send_keys("0000")
driver.find_element(By.ID, "mobile_number").send_keys("0123456789")
time.sleep(2)

print("==== User Data ====")
print(f"Title: {title_selected}")
print(f"Name: {driver.find_element(By.ID, 'first_name').get_attribute('value')}")
print(f"Last Name: {driver.find_element(By.ID, 'last_name').get_attribute('value')}")
print(f"Password: {driver.find_element(By.ID, 'password').get_attribute('value')}")
print(f"DOB: {driver.find_element(By.ID, 'days').get_attribute('value')} {driver.find_element(By.ID, 'months').get_attribute('value')} {driver.find_element(By.ID, 'years').get_attribute('value')}")
print(f"Newsletter: {'Yes' if driver.find_element(By.ID, 'newsletter').is_selected() else 'No'}")
print(f"Special Offers: {'Yes' if driver.find_element(By.ID, 'optin').is_selected() else 'No'}")
print(f"Address: {driver.find_element(By.ID, 'address1').get_attribute('value')}")
print(f"Country: {selected_country}")
print(f"State: {driver.find_element(By.ID, 'state').get_attribute('value')}")
print(f"City: {driver.find_element(By.ID, 'city').get_attribute('value')}")
print(f"Zip Code: {driver.find_element(By.ID, 'zipcode').get_attribute('value')}")
print(f"Mobile: {driver.find_element(By.ID, 'mobile_number').get_attribute('value')}")

driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/div[1]/form/button').click()
driver.save_screenshot("fullpage.png")
time.sleep(30)

message = WebDriverWait(driver, 30).until(
    EC.visibility_of_element_located((By.XPATH, "//h2/b"))
)
print (message.text)
time.sleep(10)

paragraph1 = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="form"]/div/div/div/p[1]'))
)
print (paragraph1.text)
time.sleep(10)
paragraph2 = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="form"]/div/div/div/p[2]'))
)
print (paragraph2.text)
time.sleep(10)

driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/div/a').click()
time.sleep(10)

driver.quit()
