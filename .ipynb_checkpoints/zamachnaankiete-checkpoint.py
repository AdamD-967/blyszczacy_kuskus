from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

ank = r"https://www.mentimeter.com/"
xent = r"/html/body/div[1]/div[1]/header/div/div/form/input"
xent1 = r"/html/body/div[1]/div/div[2]/div[1]/form/fieldset/div/div/input"
xsub = r"/html/body/div[1]/div/div[2]/div[1]/form/div/button"
xtest = r"/html/body/div[1]/div/div[2]/div[1]/div[2]/h1"

ran = int(input("podaj dawkę elementów: "))
code = input("podaj pin: ")
mes = input("podaj wiadomość: ")

opts = Options()
opts.add_argument('--headless')

for i in range(ran):
    driver = Chrome(options=opts)
    driver.get(ank)
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xent)))
        ent = driver.find_element_by_xpath(xent)
        ent.send_keys(code)
        ent.submit()
    except TimeoutError:
        driver.close()
        break
    
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xent1)))
        ent1 = driver.find_element_by_xpath(xent1)
        ent1.send_keys(mes)
        sub = driver.find_element_by_xpath(xsub)
        sub.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xtest)))
    except TimeoutError:
        driver.close()
        break
    try:
        driver.close()
    except:
        pass

