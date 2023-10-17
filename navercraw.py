from bs4 import BeautifulSoup
import requests


def get_soup(url):
    res = requests.get(url)
    if res.status_code == 200:
        return BeautifulSoup(res.text, 'html.parser')


def selectEx(s):
    for tags in s.select("#contentarea_left > ul > li.newsList.top > dl > dd"):
        print(tags)
        print("a txt :", tags.select_one(
            "#contentarea_left > ul > li.newsList.top > dl > dd:nth-child(2)"))
        print("여기다아아아ㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏ")


# contentarea_left > ul > li.newsList.top > dl
if __name__ == '__main__':
    s = get_soup("https://finance.naver.com/news/news_list.naver")
    selectEx(s)
# contentarea_left > ul > li.newsList.top > dl > dd:nth-child(5)
