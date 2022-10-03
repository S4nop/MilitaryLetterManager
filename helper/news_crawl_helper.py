from bs4 import BeautifulSoup
import requests
from enum import Enum

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/63.0.3239.132 Safari/537.36'}


class NaverNewsType(Enum):
    POLITIC = 0
    ECONOMY = 1
    SOCIETY = 2
    LIFECULTURE = 3
    WORLD = 4
    ITSCIENCE = 5


# TODO : cluster_group당 하나의 타이틀을 가져오도록 수정
def get_naver_news_titles(news_type):
    news_page = requests.get(f"https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=10{news_type.value}", headers=headers)
    soup = BeautifulSoup(news_page.content, "html.parser")
    texts = []
    for child in soup.select(".cluster_group > .cluster_body > ul > li > .cluster_text > .cluster_text_headline"):
        texts.append(child.get_text())
    return '\n'.join(texts)


def get_world_football_news_titles():
    news_page = requests.get("https://sports.news.naver.com/wfootball/index.nhn", headers=headers)
    soup = BeautifulSoup(news_page.content, "html.parser")
    texts = []
    for child in soup.select(".news_list > li > a"):
        texts.append(child.get_text())
    return '\n'.join(texts)


# Test code
if __name__ == "__main__":
    print(get_naver_news_titles(NaverNewsType.POLITIC))
    print(get_world_football_news_titles())