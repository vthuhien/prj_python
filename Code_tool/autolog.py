# pip install selenium webdriver-manager - codespace
# pip install selenium, pip install webdriver-manager - cmd

# if y use a server pc, you will need to install Chorme Drive 
# or use 'pip install webdriver-manager' to install it automatically
# and if y use a codespace, you will use Chrome Headless

import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



#C1 - dùng sleep
    # a = webdriver.ChromeOptions
    # driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()), options= a)
    # driver.get('https://www.pinterest.com')
    # sleep(2)

    # driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[1]/div/div[1]/div/div[2]/div[2]/button/div/div").click()
    # sleep(2)

    # driver.find_element(By.ID,"email").send_keys(email)
    # sleep(2)
    # driver.find_element(By.ID,"password").send_keys(psw)
    # sleep(2)
    # driver.quit()

#C2 - dùng WebDriverWait

file = 'key.txt'

def save_f(email,psw):
    with open(file,'w') as f:
        f.write(f'{email}\n{psw}')
    return email, psw

def load_f():
    if os.path.exists(file):
        with open(file,'r') as f:
            lines = f.readlines()
            if len(lines) >= 2:
                return lines[0].strip(), lines[1].strip()
    return None, None

def autolog(email,psw):
    a = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()), options= a)
    driver.get('https://www.pinterest.com')

    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Log in')]"))
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "email"))
        ).send_keys(email)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "password"))
        ).send_keys(psw)

        WebDriverWait(driver, 9).until(
            EC.element_to_be_clickable((By.XPATH,"//div[contains(text(),'Log in')]"))
        )

        sleep(10)

        print("Login Successful!")

    except Exception as e:
        print(f"Error during login: {e}")
    finally:
        driver.close()

email, psw = load_f()
if email and psw:
    print('Info Available')
    a = input("Do y want to change the information ? y/n").strip()
    if a == 'y':
        email = input("Enter your email: ").strip()
        psw = input("Enter ypur password: ").strip()
        save_f(email,psw)
    else :
        email = input("Enter your email: ").strip()
        psw = input("Enter ypur password: ").strip()
        save_f(email,psw)

autolog(email,psw)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              