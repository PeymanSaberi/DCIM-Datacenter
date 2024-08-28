from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import time
import re

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

        # chiller بارگذاری صفحه  4
        driver.get('url or IP address for read data of chiller')  
        time.sleep(15) # صبر کنید تا بارگذاری کامل شود  
        
        #  خواندن باکس آب خروجي
        text_box = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'panel-2')))  ##you must set id field for read data  
        text1 = text_box.text
        time.sleep(10)

        # استخراج تنها اعداد از متن  
        numbers = re.findall(r'\d+\.\d+|\d+', text1)  # ویرایش برای تشخیص اعداد اعشاری  
        if numbers:  
            data_text1 = ' '.join(numbers)  # تبدیل لیست اعداد به یک رشته  
        else:  
            data_text1 = ""  # اگر هیچ عددی پیدا نشود
        time.sleep(10)

        # خواندن باکس آب ورودي
        text_box = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'panel-5')))  ##you must set id field for read data  
        text2 = text_box.text
        time.sleep(15)

        # استخراج تنها اعداد از متن  
        numbers = re.findall(r'\d+\.\d+|\d+', text2)  # ویرایش برای تشخیص اعداد اعشاری  
        if numbers:  
            data_text2 = ' '.join(numbers)  # تبدیل لیست اعداد به یک رشته  
        else:  
            data_text2 = ""  # اگر هیچ عددی پیدا نشود

        time.sleep(10)
        
        # خواندن باکس دماي هوا
        text_box = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'panel-6'))) ##you must set id field for read data   
        text3 = text_box.text
        time.sleep(15)

        # استخراج تنها اعداد از متن  
        numbers = re.findall(r'\d+\.\d+|\d+', text3)  # ویرایش برای تشخیص اعداد اعشاری  
        if numbers:  
            data_text3 = ' '.join(numbers)  # تبدیل لیست اعداد به یک رشته  
        else:  
            data_text3 = ""  # اگر هیچ عددی پیدا نشود
        
        time.sleep(10)
        
        # کپی کردن متن به باکس دیگر  
        driver.execute_script("window.open('URL or IP  Address for report server', '_blank');")  
        time.sleep(25)  # انتظار برای باز شدن پنجره جدید  
        
        # ورود به سیستم  
        driver.switch_to.window(driver.window_handles[1])  
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "uname-box"))).send_keys("insert username")  
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "pwd-box"))).send_keys("insert password")  
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "login-button"))).click()
        time.sleep(5)

        driver.get('URL or IP Address report chillers')  
        
        # انتظار برای تکمیل ورودی  
        time.sleep(10)

        # پيدا کردن باکس آب خروجي از چيلر
        destination_box = WebDriverWait(driver, 20).until(  
            EC.presence_of_element_located((By.CSS_SELECTOR, '[id*="f1001_field1_Input1"]'))  # you must set id field for input data
        )
        time.sleep(2)

        # وارد کردن متن  
        destination_box.send_keys(data_text1)
        time.sleep(2)


        # پيدا کردن باکس آب ورودي به چيلر
        destination_box = WebDriverWait(driver, 20).until(  
            EC.presence_of_element_located((By.CSS_SELECTOR, '[id*="f1001_field2_Input1"]'))  #you must set id field for input data
        )
        time.sleep(2)

        # وارد کردن متن
        destination_box.send_keys(data_text2)
        time.sleep(2)

        # پيدا کردن باکس دماي هوا
        destination_box = WebDriverWait(driver, 20).until(  
            EC.presence_of_element_located((By.CSS_SELECTOR, '[id*="f1001_field3_Input1"]'))  #you must set id field for input data
        )
        time.sleep(3)

        # وارد کردن متن  
        destination_box.send_keys(data_text3)
        time.sleep(2)

        # شناسایی و کلیک بر روی دکمه  
        button = driver.find_element(By.XPATH, """//*[@id="button_new1001"]""")  
        button.click()
        time.sleep(5)

        #تاييد نهايي
        button = driver.find_element(By.XPATH, """//*[@id="y_1001"]""")  
        button.click()



    except Exception as e:
        print(data_text1,data_text2, data_text3)
        print(f"An error occurred: {e}")  
    finally:
        print(data_text1,'\n',data_text2, '\n',data_text3) #print for Excel report
        driver.quit()  

# اجرای تابع  
Function_All_Data_Prochista()
