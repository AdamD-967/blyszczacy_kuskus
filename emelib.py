from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time

path = r"http://cib.umed.lodz.pl/zasoby/e-ksiazki/" #strona
elibp = r"/html/body/div[3]/div/div/div[1]/table[2]/tbody/tr[3]/td[2]/a" #następny link
login = "UM160314"
haslo = "05384" #chyba
xlog = r"/html/body/div/form/div[2]/input" #login input
xpass = r"/html/body/div/form/div[6]/input" #hasło 5 
xfind = r"/html/body/div[2]/div[3]/div[1]/form/div[1]/input"
name = "Pediatria"

#opts = Options()
#opts.add_argument("--headless")
driver = Chrome()

driver.get(path)
elib = driver.find_element_by_xpath(elibp).get_attribute('href')
driver.get(elib)

log = driver.find_element_by_xpath(xlog)
log.send_keys(login)

pas = driver.find_element_by_xpath(xpass)
pas.send_keys(haslo)
pas.submit()

find = driver.find_element_by_xpath(xfind)
find.send_keys(name)
find.submit()

try:
    books = driver.find_element_by_xpath(r"/html/body/div[2]/div[2]/section/div/div/div[3]/div").find_elements_by_class_name("card ebook hoverable")
    print(books)
    for book in books:
        if book.find_element_by_xpath("/div[2]/h4/a").text != name:
            books.remove(book)
    print(books)
except:
    print(':(')

time.sleep(10)
driver.close()