import requests
import time
from parsel import Selector
from tech_news.database import create_news


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
    selector = Selector(html_content)
    next_page_link = selector.css('a.next.page-numbers::attr(href)').get()
    return next_page_link


# Requisito 4
def scrape_news(html_content):
    selector = Selector(html_content)
    news = {
        'url': selector.css('link[rel="canonical"]::attr(href)').get(),
        'title':  selector.css("h1.entry-title::text").get().strip(),
        'timestamp': selector.css('li.meta-date::text').get(),
        'writer': selector.css('span.author a::text').get(),
        'reading_time': int(
            selector.css("li.meta-reading-time::text").get().split()[0]),
        'summary': selector.xpath("string(//p)").get().strip(),
        'category': selector.css('span.label::text').get(),
    }
    return news


# Requisito 5
def get_tech_news(amount):
    url = 'https://blog.betrybe.com'
    page_content = fetch(url)
    page_links = scrape_updates(page_content)
    while len(page_links) < amount:
        url = scrape_next_page_link(page_content)
        page_content = fetch(url)
        page_links.extend(scrape_updates(page_content))
    news_content = [content for content in map(fetch, page_links[:amount])]
    news_formatted = [scrape_news(content) for content in news_content]
    create_news(news_formatted)
    return news_formatted
