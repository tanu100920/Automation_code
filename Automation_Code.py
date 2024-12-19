from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback
import time

driver_path = r"C:\Users\tanuc\Downloads\chromedriver-win64\chromedriver.exe"

service = Service(driver_path)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://quso.ai/")
    
    print(driver.page_source)
    
    email_field = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "email"))  
    )
    email_field.send_keys("your_email@example.com") 
    
    password_field = driver.find_element(By.ID, "password")  
    password_field.send_keys("your_password")  
    
    login_button = driver.find_element(By.ID, "login_button")  
    login_button.click()
    
    time.sleep(5) 
    
except Exception as e:
    print(f"An error occurred: {e}")
    traceback.print_exc()
finally:
    driver.quit()


