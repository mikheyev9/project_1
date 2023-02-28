from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os
from selenium.webdriver.common.keys import Keys



#возможно указать на вашем пк где находится драйвер для взаимодействия с браузером
#path = Service(r"/home/anton/Downloads/chromedriver_linux64/chromedriver")

#список возможных опции https://peter.sh/experiments/chromium-command-line-switches/
options = webdriver.ChromeOptions()
options.add_extension('/home/anton/env/env/BOT/work/metamask.crx')

url = 'https://app.towns.com/login'
keys = 'box journey extra tiny employ fantasy zone refuse code smooth client cliff'
list_keys = keys.split()
password = '11223344'
name = 'afonia'
email = 'gmailt@gmail.com'
issue = '2'
wallet = '0x825A6a39Bc440E0533cc211f173f657Ee0C12336'


def captcha(url):
   
    sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

    from twocaptcha import TwoCaptcha

    api_key = os.getenv('APIKEY_2CAPTCHA', '6a9c9d30266b25b963e9476c9d4521c8')

    solver = TwoCaptcha(api_key)

    try:
        result = solver.recaptcha(
            sitekey='6LdB13EeAAAAAEQ7MiLZmdG4pa28AD7K4V7x-tgG',
            invisible=1,
            url=url)
    
    except Exception as e:
        print(e)
        return False
    
    else:
        return result

with webdriver.Chrome(options=options) as driver:
    try:
        driver.get(url)
        sleep(4)
        print(driver.window_handles)
        driver.switch_to.window(driver.window_handles[0])
        
        
        driver.find_element(By.XPATH, '//button').click() # переход на метамаск
        sleep(5)
        print(driver.window_handles) # windows
        driver.switch_to.window(driver.window_handles[2]) # to metamask window
        sleep(1)
        driver.find_element(By.XPATH, "//button[contains(@class, 'btn-secondary')]").click() #import an existing
        sleep(1)
        driver.find_element(By.XPATH, '//button').click() # i agree
         
        fields = driver.find_elements(By.XPATH, '//input[@type="password"]') # field
        for i in range(len(fields)):
            fields[i].send_keys(list_keys[i])
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH , '//button').click() #send
        driver.implicitly_wait(5)
        
        passwords = driver.find_elements(By.CLASS_NAME, 'form-field__input') # 2 password fields
        for i in passwords:
            driver.implicitly_wait(1)
            i.send_keys(password)
        
        driver.find_element(By.XPATH, '//input[@type="checkbox"]').click() # chekbox
        driver.implicitly_wait(3)
        driver.find_element(By.XPATH, '//button').click() # send passwords
        sleep(5)
        
        driver.find_element(By.XPATH, '//button').click() # go it 
        button = driver.find_elements(By.XPATH, '//button')
        print('-------',button, 'buttons')
        button[2].click() # go it 
        #sleep(1500)
        driver.find_elements(By.XPATH, '//button')[2].click() # go it 
        sleep(3)
    
        
        print(driver.window_handles) #how mauch windows do we have
        driver.switch_to.window(driver.window_handles[0]) # to window 0
        sleep(1)
        driver.find_element(By.XPATH, '//button').click() # connect wallet
        sleep(4) #create winow 4
        
        print(driver.window_handles,'+++++') #how mauch windows do we have
        driver.switch_to.window(driver.window_handles[3]) # to window 4
        sleep(3)
        driver.find_element(By.XPATH, '//button[2]').click()
        driver.find_element(By.XPATH, '//button[2]').click() #click
        sleep(3)
        
        driver.switch_to.window(driver.window_handles[0]) # window 0
        sleep(2)
        driver.find_element(By.XPATH, '//button').click() #login
        sleep(3) # wait to laod the 4 window
        #sleep(10000)# open new window   
        driver.switch_to.window(driver.window_handles[3])
        driver.find_elements(By.XPATH, '//button')[1].click() # go write
        #driver.switch_to.window(driver.window_handles[2]) # are we need it??????
        sleep(1)
        print(driver.window_handles,'--------!!') #how mauch windows do we have
        driver.switch_to.window(driver.window_handles[0]) #return to win 0
        sleep(11) # moree 4 
        driver.find_element(By.XPATH, "//button[text()='Join alpha']").click() # join alpha
        sleep(3)
        
        driver.switch_to.window(driver.window_handles[3]) # what is the  nomber of this win
        driver.find_element(By.XPATH, '//button').click() # start
        driver.implicitly_wait(1)
        input = driver.find_element(By.XPATH, '//input')
        input.send_keys(name)
        driver.find_element(By.XPATH, "//button[@type='submit']").click() #next
        
        input = driver.find_element(By.XPATH, '//input')
        input.send_keys(email)
        driver.find_element(By.XPATH, "//button[@type='submit']").click() #next
        
        input = driver.find_element(By.XPATH, '//input')
        input.send_keys(issue)
        driver.find_element(By.XPATH, "//button[@type='submit']").click() #next
        sleep(1)

        checkboxes = driver.find_elements(By.XPATH, '//input') # 4 bars
        checkboxes[1].click() # select 2
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        driver.find_element(By.XPATH, '//input').send_keys(wallet)
        driver.find_element(By.XPATH, "//button[@type='submit']").click() #wallet adress next

        
        ##captcha
        WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH, "//iframe[@title='reCAPTCHA']")))
        sleep(3)
        url_now = driver.current_url
        #iframe = driver.find_element(By.XPATH, "//iframe[@title='reCAPTCHA']")
        #driver.switch_to.frame(iframe)
        #click = driver.find_element(By.CLASS_NAME, "recaptcha-checkbox-checkmark")
        #driver.execute_script("return arguments[0].scrollIntoView(true);", click)
        #click.send_keys(Keys.TAB + Keys.TAB + " ")
        

        #print(url_now)
        result = captcha(url_now)
        print(result)
        if result:
            code = result['code']

            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'g-recaptcha-response')))

            sleep(5)
            driver.execute_script(
        "document.getElementById('g-recaptcha-response').innerHTML = " + "'" + code + "'")
            driver.execute_script(f'___grecaptcha_cfg.clients[0].X.X.callback("{code}")')
            sleep(5)
            
           
           
        
        driver.find_element(By.XPATH, "//button[@type='submit']").click() #submit




        sleep(4000)
        
        sleep(1000)
        

    except Exception as ex:
        print(ex)