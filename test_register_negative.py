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

error_msg = WebDriverWait(driver, 10).until(
     EC.visibility_of_element_located((By.XPATH, "//p[contains(@class, 'error') or contains(text(), 'Email')]"))
)
    
print(f"❌ Terjadi error saat mendaftar: {error_msg.text}")
