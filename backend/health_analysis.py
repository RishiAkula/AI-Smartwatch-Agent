
import os
import json

from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY not found")

client = genai.Client(api_key=API_KEY)


def analyze_health_data(payload: dict):

    # Extract health records
    steps = payload.get("steps", [])
    sleep = payload.get("sleep", [])
    daily_totals = payload.get("daily_totals", [])

    # Prepare health data for Gemini
    health_data = {
        "steps": steps,
        "sleep": sleep,
        "daily_totals": daily_totals
    }

    prompt = f"""
    You are a personal health and wellness assistant.

    Analyze the following Apple Health data.

    HEALTH DATA:
    {json.dumps(health_data, indent=2)}

    Your tasks:

    1. Analyze daily step count.
    2. Analyze sleep duration and sleep schedule.
    3. Identify gaps in daily activity and sleep goals.
    4. Suggest practical improvements.
    5. Provide encouraging, personalized recommendations.

    Use these initial reference goals:
    - Steps: 8000 per day (adjustable target).
    - Sleep: 8 hours per night (adjustable target).

    IMPORTANT:
    - Use only the supplied health data.
    - Never invent missing measurements.
    - Clearly mention when data is unavailable.
    - Do not provide medical diagnoses.
    - Keep the report simple and actionable.

    Format the report with:
    - Overall Summary
    - Steps Analysis
    - Sleep Analysis
    - Identified Gaps
    - Recommendations
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text
