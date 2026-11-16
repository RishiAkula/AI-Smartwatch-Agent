
import os
import requests

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google import genai
from backend.health_webhook import router as health_router

from backend.classifier import classify_news_request
from backend.news import fetch_news as get_news_articles

# Load environment variables
load_dotenv()

# Get Gemini API key
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY not found in .env file")

# Initialize Gemini
client = genai.Client(api_key=API_KEY)

# Initialize FastAPI
app = FastAPI(
    title="AI Smartwatch Agent",
    description="AI-powered smartwatch assistant",
    version="1.0.0"
)
app.include_router(health_router)


class UserRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "project": "AI Smartwatch Agent",
        "status": "Running"
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


def classify_request(message: str):
    text = message.lower()

    if any(word in text for word in ["news", "headline", "breaking"]):
        return "news"

    elif any(word in text for word in ["weather", "temperature", "forecast"]):
        return "weather"

    else:
        return "general"

    
def fetch_news(query="Germany"):

    api_key = os.getenv("GNEWS_API_KEY")

    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="GNews API key is missing"
        )

    url = "https://gnews.io/api/v4/search"

    params = {
        "q": query,
        "lang": "en",
        "max": 5,
        "apikey": api_key
    }

    try:
        result = requests.get(
            url,
            params=params,
            timeout=20
        )

        result.raise_for_status()

        data = result.json()

        return data.get("articles", [])

    except requests.RequestException:
        raise HTTPException(
            status_code=502,
            detail="Unable to retrieve news from GNews"
        )






@app.post("/ask")
def ask_assistant(request: UserRequest):

    try:
        # Step 1: Detect the user's intent
        category = classify_request(request.message)

        if category == "news":

            # Step 2: Identify country and category
            details = classify_news_request(request.message)

            country = details["country"]
            news_category = details["category"]

            # Step 3: Fetch relevant news
            articles = get_news_articles(
             country=country,
             category=news_category,
             limit=5
             )

            if not articles:
                return {
                    "category": "news",
                    "agent_status": "No news found",
                    "response": "No relevant news articles found."
                }

            # Step 4: Prepare articles for Gemini
            news_context = ""

            for index, article in enumerate(articles, 1):

                news_context += f"""
                Article {index}
                Title: {article.get('title')}
                Source: {article.get('source', {}).get('name')}
                Description: {article.get('description')}
                Published: {article.get('publishedAt')}
                URL: {article.get('url')}
                """

            # Step 5: Generate AI summary
            prompt = f"""
            You are an intelligent news assistant.

            Summarize these retrieved news articles.

            Country code: {country}
            Category: {news_category}

            Instructions:
            - Use only the supplied article information.
            - Do not invent facts.
            - Explain important developments clearly.
            - Keep the summary concise.
            - Mention the article sources.

            Articles:
            {news_context}
            """

            ai_response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            # Step 6: Return everything
            return {
                "category": "news",
                "country": country,
                "news_category": news_category,
                "agent_status": "Success",
                "number_of_articles": len(articles),
                "articles": articles,
                "response": ai_response.text
            }

        # Non-news requests
        ai_response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=request.message
        )

        return {
            "category": category,
            "agent_status": "Success",
            "response": ai_response.text
        }

    except HTTPException:
        raise

    except Exception as error:
        raise HTTPException(
            status_code=502,
            detail=f"AI processing error: {str(error)}"
        )

