from selenium import webdriver #driver untuk website
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
import time
import requests
from test_login import login
from checkout_women_category import checkout_women_category
from checkout_other_category import checkout_men_category
from checkout import checkout
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://automationexercise.com/")
driver.maximize_window()

login(driver)
checkout_women_category(driver)
checkout_men_category(driver)
checkout(driver)

name_on_card = "john doe"
card_number = "1234567890"
cvc_number = "000"
expiration_month = "01"
expiration_year = "2027"

name_on_card_field = driver.find_element(By.XPATH, '//*[@id="payment-form"]/div[1]/div/input')
card_number_field = driver.find_element(By.XPATH, '//*[@id="payment-form"]/div[2]/div/input')
cvc_number_field = driver.find_element(By.XPATH, '//*[@id="payment-form"]/div[3]/div[1]/input')
expiration_month_field = driver.find_element(By.XPATH, '//*[@id="payment-form"]/div[3]/div[2]/input')
expiration_year_field = driver.find_element(By.XPATH, '//*[@id="payment-form"]/div[3]/div[3]/input')

name_on_card_field.send_keys(name_on_card)
print(name_on_card_field.get_attribute("value"))
card_number_field.send_keys(card_number)
print(card_number_field.get_attribute("value"))
cvc_number_field.send_keys(cvc_number)
print(cvc_number_field.get_attribute("value"))
expiration_month_field.send_keys(expiration_month)
print(expiration_month_field.get_attribute("value"))
expiration_year_field.send_keys(expiration_year)
print(expiration_year_field.get_attribute("value"))

time.sleep(5)
wait = WebDriverWait(driver, 10)
continue_button = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
continue_button.click()

time.sleep(5)

wait = WebDriverWait(driver, 10)
finish = wait.until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="form"]/div/div/div/p'))
)
print(finish.text)
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div/div/a').click()
time.sleep(5)