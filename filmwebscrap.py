#import pandas as pd
import requests
from bs4 import BeautifulSoup

d = dict()
n = int(input("ilość oczekiwanych wyników: "))
try:
    site = requests.get("https://www.filmweb.pl/ranking/film")
    print(site)
except:
    print(':(')
soup = BeautifulSoup(site.text, 'html.parser')
step1 = soup.find('body')
step2 = step1.find('div', class_="wrapper subpage-rankingFilm deprecated")
step3 = step2.find('div', class_="pageContent page")
step4 = step3.find('div', class_="fa__wrapper")
step5 = step4.find('section')
step6 = step5.find('div', class_="page__container")
step7 = step6.find('div', class_="wrapperContent__content")
step8 = step7.find('div', class_="ranking__list")
step9 = step8.find_all('div', class_="item place")[:n]
for e in step9:
    d[e["data-position-id"]] = dict()
    a = e.find(class_="film").find(class_="film__info").find('div', class_="film__original").string
    d[e["data-position-id"]]['title'] = a
print(d)
