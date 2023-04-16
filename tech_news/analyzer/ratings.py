from tech_news.database import search_news


# Requisito 10
def top_5_categories():
    news = search_news({"category": {"$exists": True}})
    if not news:
        return []
    categories = [new['category'] for new in news]
    print(categories)
    top_five_categories = sorted(
        set(categories), key=lambda cat: (-categories.count(cat), cat))[:5]
    print(top_five_categories)
    return top_five_categories
