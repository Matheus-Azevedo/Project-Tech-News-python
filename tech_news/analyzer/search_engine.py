from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    news = search_news({"title": {"$regex": title, "$options": "i"}})
    if not news:
        return []
    return [(new['title'], new['url']) for new in news]


# Requisito 8
def search_by_date(date):
    if not date or datetime.fromisoformat(date):
        raise ValueError("Data inválida")
    date_object = datetime.strptime(date, "%Y-%m-%d")
    date = date_object.strftime("%d/%m/%Y")
    news = search_news({"timestamp": {"$regex": date, "$options": "i"}})
    if not news:
        return []
    return [(new['title'], new['url']) for new in news]


# Requisito 9
def search_by_category(category):
    news = search_news({"category": {"$regex": category, "$options": "i"}})
    if not news:
        return []
    return [(new['title'], new['url']) for new in news]
