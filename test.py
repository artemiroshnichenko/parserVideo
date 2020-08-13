import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from selenium import webdriver
import time


URL = 'https://hdrezka.sh/films/adventures/35262-spasateli-malibu-novaya-volna-2020.html'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0', 'accept': '*/*'}
HOST = 'https://hdrezka.sh'
ua = UserAgent(verify_ssl=False)


def js(url):
    driver = webdriver.PhantomJS('/usr/local/bin/phantomjs')
    driver.get(url)
    html = driver.page_source
    return html

def init_driver():
    ff = "/usr/local/bin/chromedriver"

    driver = webdriver.Chrome(executable_path=ff)
    return driver  

def parse_url(driver):    
    driver.get(URL)
    html = driver.page_source
    return html

def write(html):
    Html_file= open("test.html","w")
    Html_file.write(html)
    Html_file.close()

if __name__ == "__main__":
    start_time=time.time()
    current_time = time.time()
    driver = init_driver()
    print("Запуск",time.time()-current_time)
    current = time.time()
    html = parse_url(driver)
    driver.close
    print("Парсинг:",time.time()-current)
    write(html)