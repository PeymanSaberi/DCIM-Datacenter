from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys  
import traceback
import pyautogui
import time
import re


def replace_standby_with_zero(input_dict):  
    """این تابع مقادیر دیکشنری را بررسی می‌کند و هر عدد 'Standby' را به 0 تبدیل می‌کند."""  
    for key, value in input_dict.items():
        
        if value == "Standby":  
            input_dict[key] = "0"  # مقدار 'Standby' را به 0 تغییر می‌دهد
            
    return input_dict  # دیکشنری اصلاح شده را برمی‌گرداند




def Function_Inrow_Collector():
    username = 'inser username'  
    password = 'inser password'  
    url = 'url or IP Address server DCIM'
    
    service = Service(r"Address in your pc\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get(url)


    try:   
        # ورود به سیستم  
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "user"))).send_keys(username)  
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "current-password"))).send_keys(password)  
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, """//*[@id="reactRoot"]/div[1]/main/div[3]/div/div[2]/div/div/form/button"""))).click()  
        time.sleep(10)
        
        driver.get("url or IP address for read data of Inrows")
        time.sleep(5)  
        
        driver.execute_script("document.body.style.zoom='50%'")  
        time.sleep(10)  

        # دیکشنری‌ها برای ذخیره‌سازی داده‌ها  
        f_data = {}  
        r_data = {}  
        s_data = {}  

        for i in range(21):  # جمع‌آوری داده‌ها از 0 تا 20  ##you must set id field for read data  
            f_key = f'f{i}'  
            r_key = f'r{i}'  
            s_key = f's{i}'
            xpath_r = f'//*[@id="{34 + i}"]/section/div[2]/div/div[1]/div/div/div[2]/div/span[1]'  
            xpath_s = f'//*[@id="{34 + i}"]/section/div[2]/div/div[2]/div/div/div[2]/div/span[1]'  
            xpath_f = f'/html/body/div/div[1]/main/div[3]/div/div/div[1]/div/div/div[1]/div/div/div[{16 + i}]/div/section/div[2]/div/div/div/div/span'  
            time.sleep(5)
            
            try:
                # Collecting data  
                f_value = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_f))).text
                r_value = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_r))).text  
                s_value = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, xpath_s))).text


                # افزودن داده‌ها به دیکشنری‌ها  
                f_data[f_key] = f_value  
                r_data[r_key] = r_value  
                s_data[s_key] = s_value                

            except Exception as e:
                print(f"Error collecting data for {i}: {e}")
                traceback.print_exc()

            #Replace standby with "0"

            f_data = replace_standby_with_zero(f_data)
            
        ##    # کپی کردن متن به باکس دیگر  
        driver.execute_script("window.open('URL or IP  Address for report server', '_blank');")  
        time.sleep(20)  # انتظار برای باز شدن پنجره جدید  
        
        # ورود به سیستم  
        driver.switch_to.window(driver.window_handles[1])  
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "uname-box"))).send_keys("insert username")  
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "pwd-box"))).send_keys("insert password")  
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "login-button"))).click()
        time.sleep(15)

        driver.get('URL or IP Address report inrows')
        
        # انتظار برای تکمیل ورودی
        time.sleep(15)

                
        #Input Inrow 1
        destination_box = WebDriverWait(driver, 5).until(  
            EC.presence_of_element_located((By.CSS_SELECTOR, '[id*="f1005_field1_Input3"]'))  # you must set id field for input data
        )
        time.sleep(3)

        # وارد کردن متن
        destination_box.send_keys(f_data['f0'])
##        time.sleep(1)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field1_Input2"]'))).send_keys(s_data['s0'])
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field1_Input1"]'))).send_keys(r_data['r0'])
        
            
        #Input Inrow 2
        destination_box = WebDriverWait(driver, 5).until(  
            EC.presence_of_element_located((By.CSS_SELECTOR, '[id*="f1005_field2_Input3"]'))  # you must set id field for input data
        )
        time.sleep(3)

        # وارد کردن متن
        destination_box.send_keys(f_data['f1'])
##        time.sleep(1)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field2_Input2"]'))).send_keys(s_data['s1'])
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field2_Input1"]'))).send_keys(r_data['r1'])


        #Input Inrow 3
        destination_box = WebDriverWait(driver, 5).until(  
            EC.presence_of_element_located((By.CSS_SELECTOR, '[id*="f1005_field3_Input3"]'))  # you must set id field for input data
        )
        time.sleep(3)

        # وارد کردن متن
        destination_box.send_keys(f_data['f2'])
##        time.sleep(1)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field3_Input2"]'))).send_keys(s_data['s2'])
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field3_Input1"]'))).send_keys(r_data['r2'])


        #Input Inrow 4
        destination_box = WebDriverWait(driver, 5).until(  
            EC.presence_of_element_located((By.CSS_SELECTOR, '[id*="f1005_field4_Input3"]'))  # you must set id field for input data
        )
        time.sleep(3)

        # وارد کردن متن
        destination_box.send_keys(f_data['f3'])
##        time.sleep(1)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field4_Input2"]'))).send_keys(s_data['s3'])
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field4_Input1"]'))).send_keys(r_data['r3'])


        #Input Inrow 5
        destination_box = WebDriverWait(driver, 5).until(  
            EC.presence_of_element_located((By.CSS_SELECTOR, '[id*="f1005_field5_Input3"]'))  # you must set id field for input data
        )
        time.sleep(3)

        # وارد کردن متن
        destination_box.send_keys(f_data['f4'])
##        time.sleep(1)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field5_Input2"]'))).send_keys(s_data['s4'])
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field5_Input1"]'))).send_keys(r_data['r4'])


        #Input Inrow 6
        destination_box = WebDriverWait(driver, 5).until(  
            EC.presence_of_element_located((By.CSS_SELECTOR, '[id*="f1005_field6_Input3"]'))  # you must set id field for input data
        )
        time.sleep(3)

        # وارد کردن متن
        destination_box.send_keys(f_data['f5'])
##        time.sleep(1)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field6_Input2"]'))).send_keys(s_data['s5'])
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field6_Input1"]'))).send_keys(r_data['r5'])



        #Input Inrow 7
        destination_box = WebDriverWait(driver, 5).until(  
            EC.presence_of_element_located((By.CSS_SELECTOR, '[id*="f1005_field7_Input3"]'))  ## you must set id field for input data
        )
        time.sleep(3)

        # وارد کردن متن
        destination_box.send_keys(f_data['f6'])
##        time.sleep(1)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field7_Input2"]'))).send_keys(s_data['s6'])
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field7_Input1"]'))).send_keys(r_data['r6'])


        #Input Inrow 8
        destination_box = WebDriverWait(driver, 5).until(  
            EC.presence_of_element_located((By.CSS_SELECTOR, '[id*="f1005_field8_Input3"]'))  ## you must set id field for input data
        )
        time.sleep(3)

        # وارد کردن متن
        destination_box.send_keys(f_data['f7'])
##        time.sleep(1)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field8_Input2"]'))).send_keys(s_data['s7'])
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field8_Input1"]'))).send_keys(r_data['r7'])
        

        #Input Inrow 9
        destination_box = WebDriverWait(driver, 5).until(  
            EC.presence_of_element_located((By.CSS_SELECTOR, '[id*="f1005_field9_Input3"]'))  # # you must set id field for input data
        )
        time.sleep(3)

        # وارد کردن متن
        destination_box.send_keys(f_data['f8'])
##        time.sleep(1)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field9_Input2"]'))).send_keys(s_data['s8'])
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field9_Input1"]'))).send_keys(r_data['r8'])      


        #Input Inrow 10
        destination_box = WebDriverWait(driver, 5).until(  
            EC.presence_of_element_located((By.CSS_SELECTOR, '[id*="f1005_field10_Input3"]'))  # # you must set id field for input data
        )
        time.sleep(3)

        # وارد کردن متن
        destination_box.send_keys(f_data['f9'])
##        time.sleep(1)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field10_Input2"]'))).send_keys(s_data['s9'])
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field10_Input1"]'))).send_keys(r_data['r9'])      


        #Input Inrow 11
        destination_box = WebDriverWait(driver, 5).until(  
            EC.presence_of_element_located((By.CSS_SELECTOR, '[id*="f1005_field11_Input3"]'))  # # you must set id field for input data
        )
        time.sleep(3)

        # وارد کردن متن
        destination_box.send_keys(f_data['f10'])
##        time.sleep(1)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field11_Input2"]'))).send_keys(s_data['s10'])
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field11_Input1"]'))).send_keys(r_data['r10'])      

        #Input Inrow 12
        destination_box = WebDriverWait(driver, 5).until(  
            EC.presence_of_element_located((By.CSS_SELECTOR, '[id*="f1005_field12_Input3"]'))  # # you must set id field for input data
        )
        time.sleep(3)

        # وارد کردن متن
        destination_box.send_keys(f_data['f11'])
##        time.sleep(1)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field12_Input2"]'))).send_keys(s_data['s11'])
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field12_Input1"]'))).send_keys(r_data['r11'])      

        # اسکرول کردن به پایین صفحه  
        body = driver.find_element("tag name", "body")  
        body.send_keys(Keys.END)
        time.sleep(5)


        #Input Inrow 12+1
        destination_box = WebDriverWait(driver, 5).until(  
            EC.presence_of_element_located((By.CSS_SELECTOR, '[id*="f1005_field13_Input3"]'))  # # you must set id field for input data
        )
        time.sleep(3)

        # وارد کردن متن
        destination_box.send_keys(f_data['f12'])
##        time.sleep(1)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field13_Input2"]'))).send_keys(s_data['s12'])
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field13_Input1"]'))).send_keys(r_data['r12'])      

        #Input Inrow 14
        destination_box = WebDriverWait(driver, 5).until(  
            EC.presence_of_element_located((By.CSS_SELECTOR, '[id*="f1005_field14_Input3"]'))  # # you must set id field for input data
        )
        time.sleep(3)

        # وارد کردن متن
        destination_box.send_keys(f_data['f13'])
##        time.sleep(1)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field14_Input2"]'))).send_keys(s_data['s13'])
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field14_Input1"]'))).send_keys(r_data['r13'])      


        #Input Inrow 15
        destination_box = WebDriverWait(driver, 5).until(  
            EC.presence_of_element_located((By.CSS_SELECTOR, '[id*="f1005_field15_Input3"]'))  ## you must set id field for input data        )
        time.sleep(3)

        # وارد کردن متن
        destination_box.send_keys(f_data['f14'])
##        time.sleep(1)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field15_Input2"]'))).send_keys(s_data['s14'])
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field15_Input1"]'))).send_keys(r_data['r14'])      


        #Input Inrow 16
        destination_box = WebDriverWait(driver, 5).until(  
            EC.presence_of_element_located((By.CSS_SELECTOR, '[id*="f1005_field16_Input3"]'))  ## you must set id field for input data
        )
        time.sleep(3)

        # وارد کردن متن
        destination_box.send_keys(f_data['f15'])
##        time.sleep(1)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field16_Input2"]'))).send_keys(s_data['s15'])
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field16_Input1"]'))).send_keys(r_data['r15'])

        
        #Input Inrow 17
        destination_box = WebDriverWait(driver, 5).until(  
            EC.presence_of_element_located((By.CSS_SELECTOR, '[id*="f1005_field17_Input3"]'))  # # you must set id field for input data
        )
        time.sleep(3)

        # وارد کردن متن
        destination_box.send_keys(f_data['f16'])
##        time.sleep(1)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field17_Input2"]'))).send_keys(s_data['s16'])
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field17_Input1"]'))).send_keys(r_data['r16'])


        #Input Inrow 18
        destination_box = WebDriverWait(driver, 5).until(  
            EC.presence_of_element_located((By.CSS_SELECTOR, '[id*="f1005_field18_Input3"]'))  ## you must set id field for input data
        )
        time.sleep(3)

        # وارد کردن متن
        destination_box.send_keys(f_data['f17'])
##        time.sleep(1)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field18_Input2"]'))).send_keys(s_data['s17'])
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field18_Input1"]'))).send_keys(r_data['r17'])


        #Input Inrow 19
        destination_box = WebDriverWait(driver, 5).until(  
            EC.presence_of_element_located((By.CSS_SELECTOR, '[id*="f1005_field19_Input3"]'))  # # you must set id field for input data
        )
        time.sleep(3)

        # وارد کردن متن
        destination_box.send_keys(f_data['f18'])
##        time.sleep(1)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field19_Input2"]'))).send_keys(s_data['s18'])
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field19_Input1"]'))).send_keys(r_data['r18'])


        #Input Inrow 20
        destination_box = WebDriverWait(driver, 5).until(  
            EC.presence_of_element_located((By.CSS_SELECTOR, '[id*="f1005_field20_Input3"]'))  # # you must set id field for input data
        )
        time.sleep(3)

        # وارد کردن متن
        destination_box.send_keys(f_data['f19'])
##        time.sleep(1)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field20_Input2"]'))).send_keys(s_data['s19'])
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field20_Input1"]'))).send_keys(r_data['r19'])


        #Input Inrow 21
        destination_box = WebDriverWait(driver, 5).until(  
            EC.presence_of_element_located((By.CSS_SELECTOR, '[id*="f1005_field21_Input3"]'))  ## you must set id field for input data
        )
        time.sleep(3)

        # وارد کردن متن
        destination_box.send_keys(f_data['f20'])
##        time.sleep(1)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field21_Input2"]'))).send_keys(s_data['s20'])
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1005_field21_Input1"]'))).send_keys(r_data['r20'])


        # شناسایی و کلیک بر روی دکمه  
        button = driver.find_element(By.XPATH, """//*[@id="button_new1005"]""")  
        button.click()
        time.sleep(5)

        #تاييد نهايي
        button = driver.find_element(By.XPATH, """//*[@id="y_1005"]""")  
        button.click()


        # نمایش دیکشنری‌ها  
        print("F Data:", f_data)
        print(f_data['f0'])
        print("R Data:", r_data)  
        print("S Data:", s_data)
        #print for Excel report
        print(r_data['r0'].strip(),"/",s_data['s0'].strip(),"/",f_data['f0'].strip(),'\n',r_data['r1'].strip(),"/",s_data['s1'].strip(),"/",f_data['f1'].strip(),'\n',r_data['r2'].strip(),"/",s_data['s2'].strip(),"/",
              f_data['f2'].strip(),'\n',r_data['r3'].strip(),"/",s_data['s3'].strip(),"/",f_data['f3'].strip(),'\n',r_data['r4'].strip(),"/",s_data['s4'].strip(),"/",f_data['f4'].strip(),'\n',r_data['r5'].strip(),"/",
              s_data['s5'].strip(),"/",f_data['f5'].strip(),'\n',r_data['r6'].strip(),"/",s_data['s6'].strip(),"/",f_data['f6'].strip(),'\n',r_data['r7'].strip(),"/",s_data['s7'].strip(),"/",
              f_data['f7'].strip(),'\n',r_data['r8'].strip(),"/",s_data['s8'].strip(),"/",f_data['f8'].strip(),'\n',r_data['r9'].strip(),"/",s_data['s9'].strip(),"/",f_data['f9'].strip(),'\n',r_data['r10'].strip(),"/",
              s_data['s10'].strip(),"/",f_data['f10'].strip(),'\n',r_data['r11'].strip(),"/",s_data['s11'].strip(),"/",f_data['f11'].strip(),'\n',r_data['r12'].strip(),"/",s_data['s12'].strip(),"/",f_data['f12'].strip(),
              '\n',r_data['r13'].strip(),"/",s_data['s13'].strip(),"/",f_data['f13'].strip(),'\n',r_data['r14'].strip(),"/",s_data['s14'].strip(),"/",f_data['f14'].strip(),'\n',r_data['r15'].strip(),
              "/",s_data['s15'].strip(),"/",f_data['f15'].strip(),'\n',r_data['r16'].strip(),"/",s_data['s16'].strip(),"/",f_data['f16'].strip(),'\n',r_data['r17'].strip(),"/",s_data['s17'].strip(),"/",f_data['f17'].strip(),
              '\n',r_data['r18'].strip(),"/",s_data['s18'].strip(),"/",f_data['f18'].strip(),'\n',r_data['r19'].strip(),"/",s_data['s19'].strip(),"/",f_data['f19'].strip(),
              '\n',r_data['r20'].strip(),"/",s_data['s20'].strip(),"/",f_data['f20'].strip())
    finally:  
        driver.quit()  # بستن مرورگر  


# فراخوانی تابع  
Function_Inrow_Collector()
