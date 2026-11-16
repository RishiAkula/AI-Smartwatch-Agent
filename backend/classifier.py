
def classify_news_request(message):

    message = message.lower()

    # Country detection
    countries = {
        "germany": "de",
        "india": "in",
        "usa": "us",
        "united states": "us",
        "uk": "gb",
        "united kingdom": "gb"
    }

    country = "de"

    for name, code in countries.items():
        if name in message:
            country = code
            break

    # Category detection
    categories = {
        "sports": ["sports", "football", "cricket", "tennis"],
        "technology": ["technology", "tech", "ai", "artificial intelligence"],
        "business": ["business", "finance", "economy"],
        "science": ["science", "research", "space"],
        "health": ["health", "medical"],
        "entertainment": ["entertainment", "movies", "films"],
        "world": ["world", "international"],
    }

    category = "general"

    for cat, keywords in categories.items():
        if any(word in message for word in keywords):
            category = cat
            break

    return {
        "country": country,
        "category": category
    }


if __name__ == "__main__":

    test_messages = [
        "Give me Germany news",
        "Show Germany football news",
        "Give me technology news in Germany",
        "Show business news in India",
        "Give me science news"
    ]

    for message in test_messages:

        result = classify_news_request(message)

        print("\nUser:", message)
        print("Agent:", result)
