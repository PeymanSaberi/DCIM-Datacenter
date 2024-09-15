from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import time
import re


def extract_numbers(text):  
    numbers = re.findall(r'\d+\.\d+|\d+', text) 
    return ' '.join(numbers) if numbers else "" 

def get_data_from_panel(driver, panel_id):  
    text_box = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, panel_id)))
    return extract_numbers(text_box.text)


def Function_All_Data_Prochista():  
    username = 'inser username'  
    password = 'inser password'  
    url = 'url or IP Address server DCIM'  
    
    service = Service(r"Address in your pc\chromedriver.exe")  
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get(url)
    

    try:  
        # عبور از هشدار امنیتی  
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "details-button"))).click()  
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "proceed-link"))).click()  

        # ورود به سیستم  
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "id_username"))).send_keys(username)  
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "id_password"))).send_keys(password)  
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Log In']"))).click()  

        # Gerator 1
        driver.get('url or IP address for read data of Generator 1')  
        time.sleep(15) # wait to load page
        
        # Read Battery Voltage
        data_text1 = get_data_from_panel(driver, 'panel-36') ##you must set id field for read data  
        data_text2 = get_data_from_panel(driver, 'panel-40') ##you must set id field for read data   

        time.sleep(5)


        ########################################################################################################

        # Gerator 2
        driver.switch_to.window(driver.window_handles[0])
        driver.get('url or IP address for read data of Generator 2')  
        time.sleep(15) # صبر کنید تا بارگذاری کامل شود  
        
        # Read Battery Voltage
        text_box = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'panel-36')))  
        text3 = text_box.text
        time.sleep(10)

        # استخراج تنها اعداد از متن  
        data_text3 = get_data_from_panel(driver, 'panel-36')  
        data_text4 = get_data_from_panel(driver, 'panel-40')  
        time.sleep(10)
        
        
        
        # کپی کردن متن به باکس دیگر  
        driver.execute_script("window.open('URL or IP  Address for report server', '_blank');")  
        time.sleep(20)  # انتظار برای باز شدن پنجره جدید  
        
        # ورود به سیستم  
        driver.switch_to.window(driver.window_handles[1])  
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "uname-box"))).send_keys("insert username")  
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "pwd-box"))).send_keys("insert password")  
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "login-button"))).click()
        time.sleep(15)

        driver.get('URL or IP Address report Generators')  
        
        # انتظار برای تکمیل ورودی
        time.sleep(15)

        #Find Battery input box Gen1
        destination_box = WebDriverWait(driver, 5).until(  
            EC.presence_of_element_located((By.CSS_SELECTOR, '[id*="f1011_field1_Input1"]'))  # you must set id field for input data
        )
        time.sleep(7)

        # وارد کردن متن
        destination_box.send_keys(data_text1)
        time.sleep(5)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1011_field1_Input2"]'))).send_keys(data_text2)   # you must set id field for input data
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1011_field2_Input1"]'))).send_keys(data_text3)   # you must set id field for input data
        WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1011_field2_Input2"]'))).send_keys(data_text4)   # you must set id field for input data
        

        # شناسایی و کلیک بر روی دکمه  
        button = driver.find_element(By.XPATH, """//*[@id="button_new1011"]""")  
        button.click()
        time.sleep(5)

        #تاييد نهايي
        button = driver.find_element(By.XPATH, """//*[@id="y_1011"]""")  
        button.click()



    except Exception as e:  
            print(data_text1,data_text2, data_text3, data_text4)  
            print(f"An error occurred: {e}")  
    finally:
        print(f"{data_text1}-{data_text2}",'\n'f"{data_text3}-{data_text4}")  #print for Excel report
        driver.quit()  

Function_All_Data_Prochista()


