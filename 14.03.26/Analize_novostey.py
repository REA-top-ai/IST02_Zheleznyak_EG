import requests
import json


def analyze_news(api_key, search_query="news"):

    url = "https://newsapi.org/v2/everything"
    params = {
        'q': search_query,
        'apiKey': api_key,
        'pageSize': 100,
        'language': 'ru'
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()
        articles = data.get('articles', [])
    except Exception as e:
        print(f"Ошибка: {e}")
        return []

    results = []

    for article in articles:
        title = article.get('title')
        if not title or not title.strip():
            continue

        url = article.get('url')
        if not url or not url.startswith(('http://', 'https://')):
            continue

        description = article.get('description')
        if not description or len(description) < 50:
            continue

        results.append({
            "title": title.strip(),
            "source": article.get('source', {}).get('name', 'Unknown'),
            "publishedat": article.get('publishedAt', ''),
            "Author": article.get('author') or 'Unknown'
        })

        if len(results) >= 50:
            break

    return results


if __name__ == "__main__":
    API_KEY = "60c8f98871a242b692f4c043bf07ec24"

    news = analyze_news(API_KEY, "technology")

    print(json.dumps(news, ensure_ascii=False, indent=2))

    with open('news.json', 'w', encoding='utf-8') as f:
        json.dump(news, f, ensure_ascii=False, indent=2)

    print(f"\nВсего отобрано статей: {len(news)}")
else:
    print("Пожалуйста, укажите ваш API ключ NewsAPI")