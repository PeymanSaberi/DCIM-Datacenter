from selenium import webdriver  
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.chrome.service import Service  
from selenium.webdriver.support import expected_conditions as EC  
import time  
import re  

def extract_numbers(text):  
    """Extracts numbers from a given text."""  
    numbers = re.findall(r'\d+\.\d+|\d+', text)  
    return ' '.join(numbers) if numbers else ""  

def get_data_from_panel(driver, panel_id):  
    """Fetches and extracts numbers from a panel."""  
    try:  
        # Use WebDriverWait to ensure the element is present  
        text_box = WebDriverWait(driver, 20).until(  
            EC.presence_of_element_located((By.ID, panel_id))  
        )  
        return extract_numbers(text_box.text)  # Ensure text_box is a WebElement  
    except Exception as e:  
        print(f"Error retrieving data from panel {panel_id}: {e}")  
        return ""  

def input_panel_data(driver, field_ids, values):  
    """Inputs data into specified fields."""  
    for field_id, value in zip(field_ids, values):  
        input_field = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, field_id)))  
        input_field.clear()  
        input_field.send_keys(value)  


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

        
        # Navigate to the data panel page  
        driver.get('url or IP address for read data of ups 1')  
        time.sleep(23)
    
   
        # Read Output Voltage UPSITA    ##you must set id field for read data  
        Av1 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/grafana-app/div/div/react-container/div/div[2]/div/div[1]/div/div/div[33]/div/div[1]/div/div[2]/div/div/div/div/div/div/span[1]'))).text
        Av2 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/grafana-app/div/div/react-container/div/div[2]/div/div[1]/div/div/div[34]/div/div[1]/div/div[2]/div/div/div/div/div/div/span[1]'))).text
        Av3 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/grafana-app/div/div/react-container/div/div[2]/div/div[1]/div/div/div[35]/div/div[1]/div/div[2]/div/div/div/div/div/div/span[1]'))).text
        


        # Read Output Power UPSITA   ##you must set id field for read data  
        Ap1 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/grafana-app/div/div/react-container/div/div[2]/div/div[1]/div/div/div[50]/div/div[1]/div/div[2]/div/div/div/div/div/div/span[1]'))).text
        Ap2 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/grafana-app/div/div/react-container/div/div[2]/div/div[1]/div/div/div[51]/div/div[1]/div/div[2]/div/div/div/div/div/div/span[1]'))).text
        Ap3 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/grafana-app/div/div/react-container/div/div[2]/div/div[1]/div/div/div[52]/div/div[1]/div/div[2]/div/div/div/div/div/div/span[1]'))).text

        ##you must set id field for read data  
        Af1 = get_data_from_panel(driver, 'panel-45')   

        # Print all retrieved values  
        print("Output Voltages:", Av1, Av2, Av3)  
        print("Output Powers:", Ap1, Ap2, Ap3)  
        print("Frequency:", Af1)
        
        time.sleep(7)  # Allow for data retrieval before processing it 

        # Read UPSITB
        driver.switch_to.window(driver.window_handles[0])
        driver.get('url or IP address for read data of ups 2')
        time.sleep(10)  # صبر کنید تا بارگذاری کامل شود

        # Read Output Voltage UPSITB  ##you must set id field for read data  
        Bv1 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/grafana-app/div/div/react-container/div/div[2]/div/div[1]/div/div/div[33]/div/div[1]/div/div[2]/div/div/div/div/div/div/span[1]'))).text
        Bv2 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/grafana-app/div/div/react-container/div/div[2]/div/div[1]/div/div/div[34]/div/div[1]/div/div[2]/div/div/div/div/div/div/span[1]'))).text
        Bv3 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/grafana-app/div/div/react-container/div/div[2]/div/div[1]/div/div/div[35]/div/div[1]/div/div[2]/div/div/div/div/div/div/span[1]'))).text

        # Read Output Power UPSITB  ##you must set id field for read data  
        Bp1 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/grafana-app/div/div/react-container/div/div[2]/div/div[1]/div/div/div[50]/div/div[1]/div/div[2]/div/div/div/div/div/div/span[1]'))).text
        Bp2 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/grafana-app/div/div/react-container/div/div[2]/div/div[1]/div/div/div[51]/div/div[1]/div/div[2]/div/div/div/div/div/div/span[1]'))).text
        Bp3 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/grafana-app/div/div/react-container/div/div[2]/div/div[1]/div/div/div[52]/div/div[1]/div/div[2]/div/div/div/div/div/div/span[1]'))).text

        # Read Freq. UPSITB  ##you must set id field for read data  
        Bf1 = get_data_from_panel(driver, 'panel-45')

        

        print("Output Voltages:", Bv1, Bv2, Bv3)  
        print("Output Powers:", Bp1, Bp2, Bp3)  
        print("Frequency:", Bf1)

        # Read UPSNonIT1
        driver.switch_to.window(driver.window_handles[0])
        driver.get('url or IP address for read data of ups 3')
        WebDriverWait(driver, 20)  # صبر کنید تا بارگذاری کامل شود

        # Read Output Voltage LL UPSNonIT1  ##you must set id field for read data  V = voltag for RST  v = voltag for only one phase
        CV1 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/grafana-app/div/div/react-container/div/div[2]/div/div[1]/div/div/div[48]/div/div[1]/div/div[2]/div/div/div/div/div/div/span[1]'))).text
        CV2 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/grafana-app/div/div/react-container/div/div[2]/div/div[1]/div/div/div[49]/div/div[1]/div/div[2]/div/div/div/div/div/div/span[1]'))).text
        CV3 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/grafana-app/div/div/react-container/div/div[2]/div/div[1]/div/div/div[50]/div/div[1]/div/div[2]/div/div/div/div/div/div/span[1]'))).text

        # Read Output Power UPSNonIT1  ##you must set id field for read data  
        Cp = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/grafana-app/div/div/react-container/div/div[2]/div/div[1]/div/div/div[55]/div/div[1]/div/div[2]/div/div/div/div/div/div/span[1]'))).text

        # Read Output voltage LN  ##you must set id field for read data  
        Cv1 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/grafana-app/div/div/react-container/div/div[2]/div/div[1]/div/div/div[32]/div/div[1]/div/div[2]/div/div/div/div/div/div/span[1]'))).text
        Cv2 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/grafana-app/div/div/react-container/div/div[2]/div/div[1]/div/div/div[33]/div/div[1]/div/div[2]/div/div/div/div/div/div/span[1]'))).text
        Cv3 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/grafana-app/div/div/react-container/div/div[2]/div/div[1]/div/div/div[34]/div/div[1]/div/div[2]/div/div/div/div/div/div/span[1]'))).text

        print("Output Voltages:", Cv1, Cv2, Cv3)  
        print("Output Powers:", CV1, CV2, CV3)  
        print("Frequency:", Cp)
        WebDriverWait(driver, 25)

        # Read UPSNonIT2  ##you must set id field for read data  
        driver.switch_to.window(driver.window_handles[0])
        driver.get('url or IP address for read data of ups 4')
        WebDriverWait(driver, 20)  # صبر کنید تا بارگذاری کامل شود

        # Read Output Voltage LL UPSNonIT2  ##you must set id field for read data  
        DV1 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/grafana-app/div/div/react-container/div/div[2]/div/div[1]/div/div/div[48]/div/div[1]/div/div[2]/div/div/div/div/div/div/span[1]'))).text
        DV2 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/grafana-app/div/div/react-container/div/div[2]/div/div[1]/div/div/div[49]/div/div[1]/div/div[2]/div/div/div/div/div/div/span[1]'))).text
        DV3 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/grafana-app/div/div/react-container/div/div[2]/div/div[1]/div/div/div[50]/div/div[1]/div/div[2]/div/div/div/div/div/div/span[1]'))).text

        # Read Output Power UPSNonIT2  ##you must set id field for read data  
        Dp = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/grafana-app/div/div/react-container/div/div[2]/div/div[1]/div/div/div[55]/div/div[1]/div/div[2]/div/div/div/div/div/div/span[1]'))).text

        # Read Output voltage LN  ##you must set id field for read data  
        Dv1 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/grafana-app/div/div/react-container/div/div[2]/div/div[1]/div/div/div[32]/div/div[1]/div/div[2]/div/div/div/div/div/div/span[1]'))).text
        Dv2 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/grafana-app/div/div/react-container/div/div[2]/div/div[1]/div/div/div[33]/div/div[1]/div/div[2]/div/div/div/div/div/div/span[1]'))).text
        Dv3 = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/grafana-app/div/div/react-container/div/div[2]/div/div[1]/div/div/div[34]/div/div[1]/div/div[2]/div/div/div/div/div/div/span[1]'))).text
        time.sleep(10)

        print("Output Voltages:", Dv1, Dv2, Dv3)  
        print("Output Powers:", DV1, DV2, DV3)  
        print("Frequency:", Dp)

        # محاسبات کلی
        try:
            Av1, Av2, Av3, Ap1, Ap2, Ap3, Af1, Bv1, Bv2, Bv3, Bp1, Bp2, Bp3, Bf1, CV1, CV2, CV3, Cv1, Cv2 , Cv3, Cp, DV1, DV2, DV3, Dv1, Dv2, Dv3, Dp = map(float, [Av1, Av2, Av3, Ap1, Ap2, Ap3,
                                                                                                                                                                    Af1, Bv1, Bv2, Bv3, Bp1, Bp2, Bp3, Bf1,
                                                                                                                                                                    CV1, CV2, CV3, Cv1, Cv2 , Cv3, Cp, DV1,
                                                                                                                                                                    DV2,DV3, Dv1, Dv2, Dv3, Dp])
            time.sleep(3)
            TotalAV = round((Av1 + Av2 + Av3) / 3, 1)
            TotalAP = Ap1 + Ap2 + Ap3
            TotalAv = "221"
            TotalBV = round((Bv1 + Bv2 + Bv3) / 3, 1)
            TotalBP = Bp1 + Bp2 + Bp3
            TotalBv = "220.5"
            TotalCV = round((CV1 + CV2 + CV3) / 3, 1)
            TotalCv = round((Cv1 + Cv2 + Cv3) / 3, 1)
            TotalDV = round((DV1 + DV2 + DV3) / 3, 1)
            TotalDv = round((Dv1 + Dv2 + Dv3) / 3, 1)

        except ZeroDivisionError:
            TotalAV = 0

        # کپی کردن متن به باکس دیگر  
        driver.execute_script("window.open('URL or IP  Address for report server1', '_blank');")  
        time.sleep(25)  # انتظار برای باز شدن پنجره جدید  
        
        # ورود به سیستم  
        driver.switch_to.window(driver.window_handles[1])  
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "uname-box"))).send_keys("insert username")  
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "pwd-box"))).send_keys("insert password")  
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "login-button"))).click()
        time.sleep(5)

        driver.get('URL or IP Address report ups')  
        
        # انتظار برای تکمیل ورودی  
        time.sleep(10)

        # Input KW UPSITA
        destination_box = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[id*="f1018_field1_Input4"]')) # you must set id fields for input data
            )
        time.sleep(7)
##        destination_box.clear()  # اطمینان از پاک بودن فیلد  
        destination_box.send_keys(TotalAP)
        time.sleep(5)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1018_field1_Input3"]'))).send_keys(Af1)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1018_field1_Input2"]'))).send_keys(TotalAv)
        WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1018_field1_Input1"]'))).send_keys(TotalAV)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1018_field2_Input4"]'))).send_keys(TotalBP)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1018_field2_Input3"]'))).send_keys(Bf1)
        WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1018_field2_Input2"]'))).send_keys(TotalBv)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1018_field2_Input1"]'))).send_keys(TotalBV)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1018_field3_Input4"]'))).send_keys(Cp)
        WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1018_field3_Input3"]'))).send_keys(Af1)
        WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1018_field3_Input2"]'))).send_keys(TotalCv)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1018_field3_Input1"]'))).send_keys(TotalCV)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1018_field4_Input4"]'))).send_keys(Dp)
        WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1018_field4_Input3"]'))).send_keys(Af1)
        WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1018_field4_Input2"]'))).send_keys(TotalDv)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id*="f1018_field4_Input1"]'))).send_keys(TotalDV)



        time.sleep(5)
        # Save
        button = driver.find_element(By.XPATH, """//*[@id="button_new1018"]""")
        button.click()
        time.sleep(5)

        # تایید نهایی
        button = driver.find_element(By.XPATH, """//*[@id="y_1018"]""")
        button.click()



        # Make sure to quit the driver in the finally block  
    except Exception as e:
        print(f"An error occurred: {e}")


        
    finally:
        print("Af1",Af1, "\nTotalAv", TotalAv, "\nTotalAV", TotalAV, "\nTotalBP", TotalBP, "\nBf1", Bf1, "\nTotalBv",TotalBv, "\nTotalBV", TotalBV, "\nCP", Cp, "\nTotalCv",TotalCv, "\nTotalCV", TotalCV,"\nDP",Dp, "\nTotalDv",TotalDv, "\nTotalDV", TotalDV)
        print(f"{TotalAV}-{TotalAv}-{Af1}-{TotalAP}",'\n'f"{TotalBV}-{TotalBv}-{Bf1}-{TotalBP}",'\n'f"{TotalCV}-{TotalCv}-{Af1}-{Cp}",'\n'f"{TotalDV}-{TotalDv}-{Af1}-{Dp}")  # print for Excel report
        driver.quit()  # Ensure the driver is closed regardless of success or failure  

# Call the main function  
if __name__ == "__main__":  
    Function_All_Data_Prochista()
