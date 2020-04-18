from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

path = r"http://cib.umed.lodz.pl/zasoby/e-ksiazki/" #strona
elibp = r"/html/body/div[3]/div/div/div[1]/table[2]/tbody/tr[3]/td[2]/a" #następny link
login = "UM160314"
haslo = "05384" 
xlog = r"/html/body/div/form/div[2]/input" #login input
xpass = r"/html/body/div/form/div[6]/input" #hasło 5 
isbn = "9788366310551"
xfind = r"/html/body/div[2]/div[3]/div[1]/form/div[1]/input" #zaawansowane wyszukiwanie
xpdf = r"/html/body/div[2]/div[2]/section/div/div/div[3]/div/div/div[2]/div/div/div/a[1]" #przycisk zobacz pdf
xbutton = r"/html/body/web-reader/doc-view/div/div/footer-view/div/nav-view/div[2]/div/div/button[2]" #przycisk do scrollowania przez książkę
xins = r"/html/body/web-reader/doc-view/div/div/footer-view/div/nav-view/div[2]/div/div/span[1]/input" #input do scrollowania
xpage = r"/html/body/div[1]/div[2]/div[5]/div[2]/div[2]/div/div"

#opts = Options()
#opts.add_argument("--headless")
driver = Chrome()

driver.get(path)
elib = driver.find_element_by_xpath(elibp).get_attribute('href')
driver.get(elib)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xlog)))
log = driver.find_element_by_xpath(xlog)
log.send_keys(login)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpass)))
pas = driver.find_element_by_xpath(xpass)
pas.send_keys(haslo)
pas.submit()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xfind)))
find = driver.find_element_by_xpath(xfind)
find.send_keys(isbn)
find.submit()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpdf)))
lin = driver.find_element_by_xpath(xpdf).get_attribute("href")
driver.get(lin)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpage)))
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xbutton)))
button = driver.find_element_by_xpath(xbutton)
button.click()

sleep(10)
driver.close()