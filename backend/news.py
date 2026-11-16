
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GNEWS_API_KEY")

NEWS_URL = "https://gnews.io/api/v4/top-headlines"



def fetch_news(country="de", category="general", limit=5):

    if not API_KEY:
        raise ValueError("GNews API key missing")

    params = {
        "country": country,
        "category": category,
        "max": limit,
        "apikey": API_KEY
    }

    response = requests.get(
        NEWS_URL,
        params=params,
        timeout=20
    )

    response.raise_for_status()

    data = response.json()

    return data.get("articles", [])



if __name__ == "__main__":

    articles = fetch_news(
        country="de",
        category="general",
        limit=5
    )

    print("\n===== AI NEWS AGENT =====\n")

    for index, article in enumerate(articles, 1):

        print(f"{index}. {article.get('title')}")
        print(f"Source: {article.get('source', {}).get('name')}")
        print(f"Description: {article.get('description')}")
        print(f"URL: {article.get('url')}")

        print("-" * 60)
