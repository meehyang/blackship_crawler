import sys
import requests
import pymysql
from xvfbwrapper import Xvfb
from selenium import webdriver
from bs4 import BeautifulSoup

URL = "https://ameblo.jp/blackship-staff/page-%d.html"

def connect_database():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='acs', database='blackship_crawler')
    if conn.cursor() is None:
        print("db connection error")
        conn.close()
    else:
        print("db connect success")


# chromedriver headless 모드로 띄우기 
def make_chrome_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    
    driver = webdriver.Chrome('./bin/chromedriver', options = options)
    driver.implicitly_wait(3)

    return driver

# driver 끄기
def close_chrome_driver(driver):
    driver.quit()

# driver에 해당 url 로딩 후 source 리턴 
def get_url(driver, url, page):
    driver.get(URL % page)
    
    return driver.page_source

def html_parse(req):
    soup = BeautifulSoup(req, 'html.parser')
    article_titles = soup.select('#main > div > article > div > div > div > div.skinArticleHeader > div > h1 > a')
    article_infos = soup.select('#main > div > article > div > div > div > div.skinArticleBody > div > div.articleDetailArea.skinWeakColor')
    article_bodies = soup.select('#main > div > article > div > div > div > div.skinArticleBody > div.skinArticleBody2 > div.articleText')

    images = []
    titles = []
    for article_body in article_bodies:
        if "福山潤" in article_body.text:
            images.append(article_body.find_all('img'))
            for article_title in article_titles:
                titles.append(article_title)

    # 태그 달린 형태의 값들 title
    print(images)
    print(titles)

def main():
    # driver 없이 html 파싱해서 게시 시간 체크 
    # db 연결해서 crawler 최신 record의 latest_board_date 보다 최근 게시물이 있다면
    # make_chrome_driver
    # get url from virtual chrome driver
    # html parsing
    # get data
    # if new twitter mention

    driver = make_chrome_driver()
    req = get_url(driver, URL, 2)
    html_parse(req)
    close_chrome_driver(driver)

if __name__ == "__main__":
    main()
    # connect_database()
    

