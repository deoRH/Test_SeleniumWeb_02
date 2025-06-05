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

email = "salah@mail.com"
password = "salah"

email_field = driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div[1]/form/input[2]')
password_field = driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div[1]/form/input[3]')

email_field.send_keys(email)
password_field.send_keys(password)

driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[1]/div[1]/form/button').click()
time.sleep(5)

wait = WebDriverWait(driver, 10)
login_failed = wait.until(
    EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Your email or password is incorrect')]"))
)
print(login_failed.text)
