import pandas as pd
import requests
from bs4 import BeautifulSoup

d = dict()
n = int(input("ilość początek zakresu: "))-1
m = int(input("podaj koniec zakresu: "))
try:
    site = requests.get("https://www.filmweb.pl/ranking/film")
    print(site)
except:
    print(':(')
try:
    soup = BeautifulSoup(site.text, 'html.parser')
    step1 = soup.find('body')
    step2 = step1.find('div', class_="wrapper subpage-rankingFilm deprecated")
    step3 = step2.find('div', class_="pageContent page")
    step4 = step3.find('div', class_="fa__wrapper")
    step5 = step4.find('section')
    step6 = step5.find('div', class_="page__container")
    step7 = step6.find('div', class_="wrapperContent__content")
    step8 = step7.find('div', class_="ranking__list")
    step9 = step8.find_all('div', class_="item place")[n:m]
    for e in step9:
        d[e["data-position-id"]] = dict()
        a = e.find(class_="film")
        b = a.find(class_="film__info") .find('h3', class_="film__title").find('a').string
        d[e["data-position-id"]]['title'] = b
        c = a.find('div').find('h3').find(class_="film__production-year").string
        d[e["data-position-id"]]['year'] = c
    print(pd.DataFrame.from_dict(d, orient='index'))
except:
    print("went wrong :(")
