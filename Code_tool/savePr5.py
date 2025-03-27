import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


file = 'tk.txt'
def save_f(email,psw):
    with open('tk.txt', 'w') as f:
        f.write(f"{email}\n{psw}")
    return email,psw

def load_f():
    if os.path.exists(file):
        with open('tk.txt', 'r') as f:
            line = f.readlines()
            if len(line) >= 2:
                return line[0].strip(),line[1].strip()
    return None
        
def auto_log(email,psw):
    a = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()), options = a)

    driver.get('https://www.pinterest.com')

    WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Log in')]"))
    ).click()

    WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.ID,"email"))
    ).send_keys(email)

    WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.ID,"password"))
    ).send_keys(psw)

    WebDriverWait(driver,10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Log in')]"))
    ).click()

email,psw = load_f()
if not email and psw:
    email = input("Enter your email: ")
    psw = input("Enter your psw: ")
    email,psw = save_f(email,psw)
else:
    print("info avaliable")

