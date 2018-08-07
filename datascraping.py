from selenium import webdriver
import time
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS()
url = 'http://www.1zplay.com/score?category=csgo&state=active'
driver.get(url)

time.sleep(5)

html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
soup = BeautifulSoup(html, 'html.parser')
games = soup.find_all(class_='col-xs-12 schedule-upcoming')

for game in games:
    for names in game:
        print(names.get('b'))