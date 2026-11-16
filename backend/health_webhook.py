
import json
from datetime import date
from pathlib import Path
from fastapi import APIRouter, HTTPException, Body
from backend.health_analysis import analyze_health_data
from backend.gmail_service import send_email
from dotenv import load_dotenv
import os

load_dotenv()

router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent.parent
TRACKER_FILE = BASE_DIR / "report_tracker.json"


def get_last_report_date():
    if not TRACKER_FILE.exists():
        return None

    with open(TRACKER_FILE, "r") as file:
        data = json.load(file)

    return data.get("last_report_date")


def update_last_report_date():
    with open(TRACKER_FILE, "w") as file:
        json.dump(
            {"last_report_date": date.today().isoformat()},
            file,
            indent=4
        )


@router.post("/webhooks/apple-health")
async def receive_health_data(payload: dict = Body(...)):

    if not isinstance(payload, dict):
        raise HTTPException(
            status_code=400,
            detail="Expected a JSON object"
        )

    steps = payload.get("steps", [])
    sleep = payload.get("sleep", [])
    daily_totals = payload.get("daily_totals", [])

    if not all(isinstance(x, list) for x in [steps, sleep, daily_totals]):
        raise HTTPException(
            status_code=400,
            detail="Steps, sleep and daily_totals must be lists"
        )

    # Step 1: Analyze health data using Gemini
    ai_analysis = analyze_health_data(payload)
    # Step 2: Send only one report per day
    recipient = os.getenv("HEALTH_REPORT_EMAIL")
    today = date.today().isoformat()
    last_report_date = get_last_report_date()

    if not recipient:
        email_result = {
            "status": "skipped",
            "message": "No recipient configured"
        }

    elif not (steps or sleep or daily_totals):
        email_result = {
            "status": "skipped",
            "message": "No health records available"
        }

    elif last_report_date == today:
        email_result = {
            "status": "skipped",
            "message": "Today's health report has already been sent"
        }

    else:
        try:
            email_result = send_email(
                recipient,
                "Your AI Smartwatch Health Report",
                ai_analysis
            )

            update_last_report_date()

        except Exception as e:
            print(f"EMAIL SENDING FAILED: {e}")
            email_result = {
                "status": "failed",
                "message": "Health analysis completed, but email delivery failed."
            }

    # Step 3: Prepare final response
    response = {
        "status": "success",
        "message": "Apple Health data received and analyzed!",
        "source": payload.get("source"),
        "steps_records": len(steps),
        "sleep_records": len(sleep),
        "daily_totals_records": len(daily_totals),
        "steps_sample": steps[:2],
        "sleep_sample": sleep[:2],
        "daily_totals_sample": daily_totals[:2],
        "ai_analysis": ai_analysis,
        "email_status": email_result
    }

    print("APPLE HEALTH DATA RECEIVED")
    print(response)

    return response
