import requests
import time
from parsel import Selector
# from bs4 import BeautifulSoup


# Requisito 1
def fetch(url: str) -> str:
    headers = {'user-agent': 'Fake user-agent'}
    time.sleep(1)
    try:
        response = requests.get(url, headers=headers, timeout=3)
        response.raise_for_status()
    except (requests.HTTPError, requests.ConnectionError, requests.Timeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_updates(html_content: str) -> list:
    selector = Selector(html_content)
    links = selector.css('h2.entry-title a::attr(href)').getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
