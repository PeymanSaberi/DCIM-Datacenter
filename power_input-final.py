from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import logging
import time
import re


logging.basicConfig(level=logging.INFO)


def extract_numbers(text):  
    numbers = re.findall(r'\d+\.\d+|\d+', text)
    return ' '.join(numbers) if numbers else ""  

def get_data_from_panel(driver, panel_id):  
    text_box = WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.ID, panel_id)))  
    return extract_numbers(text_box.text)  

def input_data(driver, KW, TotalA):  
    driver.get('URL or IP Address report power module')  
    WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.CSS_SELECTOR, "[id*='f1002_field1_Input1']")))  
    driver.find_element(By.CSS_SELECTOR, "[id*='f1002_field1_Input1']").send_keys(round(KW, 1))
    time.sleep(10)

    additional_values = ["161.6", "44", round(TotalA, 1), "247.1", "50"]  
    for i, value in enumerate(additional_values, start=2):  
        input_field = WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.CSS_SELECTOR, f"[id*='f1002_field{i}_Input1']")))  
        #input_field.clear()  
        input_field.send_keys(value)
        
    time.sleep(10)
    driver.find_element(By.XPATH, '//*[@id="button_new1002"]').click()
    time.sleep(5)
    WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="y_1002"]'))).click()  

def Function_All_Data_Prochista():
    username = 'inser username'  
    password = 'inser password'  
    url = 'url or IP Address server DCIM'   
    service = Service(r"Address in your pc\chromedriver.exe")  
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get(url)
    

    try:  
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "details-button"))).click()  
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "proceed-link"))).click()  
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, "id_username"))).send_keys(username)  
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, "id_password"))).send_keys(password)  
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Log In']"))).click()  

        driver.get('url or IP address for read data of power 1')  
        time.sleep(25)  

        A = get_data_from_panel(driver, 'panel-16')   ##you must set id field for read data  
        RA = get_data_from_panel(driver, 'panel-2')   ##you must set id field for read data  
        SA = get_data_from_panel(driver, 'panel-41')  ##you must set id field for read data  
        TA = get_data_from_panel(driver, 'panel-42')  ##you must set id field for read data  

        driver.get('url or IP address for read data of power 2')  
        time.sleep(15)  

        B = get_data_from_panel(driver, 'panel-16')  ##you must set id field for read data  
        RB = get_data_from_panel(driver, 'panel-2')  ##you must set id field for read data  
        SB = get_data_from_panel(driver, 'panel-41') ##you must set id field for read data   
        TB = get_data_from_panel(driver, 'panel-42') ##you must set id field for read data   

        RA, RB, SA, SB, TA, TB = map(float, [RA, RB, SA, SB, TA, TB])  
        A, B = map(float, [A, B])  
        KW = A + B  
        TotalA = (RA + RB + SA + SB + TA + TB) / 3  

        driver.execute_script("window.open('URL or IP  Address for report server', '_blank');")  
        time.sleep(17)  
        driver.switch_to.window(driver.window_handles[1])  

        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "uname-box"))).send_keys("insert usernam")  
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "pwd-box"))).send_keys("insert password")  
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "login-button"))).click()  
        time.sleep(15)  

        input_data(driver, KW, TotalA)  

    except Exception as e:  
        print(f"Error occurred: {e}")

    finally:
        print("KW =", KW, "\ntotalA =", round(TotalA, 1), "\nRAB =", (RA + RB), "\nSAB=", (SA + SB), "\nTAB=", (TA + TB))
        print(str(RA + RB).strip(),"/",str(SA + SB).strip(),"/",str(TA + TB).strip()) #print for Excel report
        driver.quit()  

Function_All_Data_Prochista()

