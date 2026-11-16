
import streamlit as st
import os
from datetime import date
from dotenv import load_dotenv

from backend.health_analysis import analyze_health_data
from backend.gmail_service import send_email

load_dotenv()

st.set_page_config(
    page_title="AI Smartwatch Agent",
    page_icon="⌚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------- DESIGN --------------------

st.markdown("""
<style>
.stApp {
    background: #0b1020;
    color: #f1f5f9;
}
[data-testid="stSidebar"] {
    background: #111827;
    border-right: 1px solid #263248;
}
.block-container {
    padding-top: 2rem;
    max-width: 1450px;
}
.hero {
    background: linear-gradient(120deg, #172554, #312e81, #164e63);
    padding: 30px;
    border-radius: 18px;
    border: 1px solid #374b79;
    margin-bottom: 25px;
}
.hero h1 {
    color: white;
    font-size: 32px;
    margin-bottom: 8px;
}
.hero p {
    color: #cbd5e1;
    font-size: 15px;
}
.metric-card {
    background: linear-gradient(145deg, #172033, #111827);
    border: 1px solid #29364d;
    border-radius: 16px;
    padding: 22px;
    min-height: 145px;
}
.metric-label {
    color: #94a3b8;
    font-size: 14px;
}
.metric-value {
    color: white;
    font-size: 30px;
    font-weight: 700;
    margin-top: 12px;
}
.metric-note {
    color: #34d399;
    font-size: 12px;
    margin-top: 8px;
}
.panel {
    background: #111827;
    border: 1px solid #29364d;
    border-radius: 16px;
    padding: 22px;
    margin-top: 12px;
}
.small-muted {
    color: #94a3b8;
    font-size: 13px;
}
div.stButton > button {
    background: linear-gradient(90deg, #6366f1, #0891b2);
    color: white;
    border: none;
    border-radius: 9px;
    font-weight: 600;
    padding: 10px 20px;
}
div.stButton > button:hover {
    border: 1px solid #67e8f9;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# -------------------- SAMPLE DATA --------------------

health_data = {
    "source": "Apple Health Demo",
    "steps": [{"date": str(date.today()), "count": 8500}],
    "sleep": [{"date": str(date.today()), "duration_hours": 7.5}],
    "daily_totals": [{
        "date": str(date.today()),
        "steps": 8500,
        "sleep_hours": 7.5
    }]
}

steps = 8500
sleep_hours = 7.5
step_goal = 10000
sleep_goal = 8

step_progress = min(steps / step_goal, 1.0)
sleep_progress = min(sleep_hours / sleep_goal, 1.0)

# -------------------- SIDEBAR --------------------

with st.sidebar:
    st.markdown("## ⌚ SMARTWATCH AI")
    st.caption("PERSONAL HEALTH INTELLIGENCE")
    st.divider()

    page = st.radio(
        "WORKSPACE",
        ["Overview", "AI Health Insights", "Email Reports"],
        label_visibility="collapsed"
    )

    st.divider()
    st.markdown("### System Status")

    st.markdown("🟢 Gemini AI")
    st.markdown("🟢 Gmail Integration")
    st.markdown("🟢 FastAPI Backend")

    st.divider()
    st.caption("AI Smartwatch Agent")
    st.caption("Powered by Python + Gemini")

# -------------------- HERO --------------------

st.markdown(f"""
<div class="hero">
    <h1>⌚ Your Health, Intelligently Connected.</h1>
    <p>AI-powered personal wellness insights, activity monitoring
    and intelligent health reporting.</p>
    <p>📅 {date.today().strftime("%A, %d %B %Y")}
    &nbsp; | &nbsp; 🟢 Demo environment</p>
</div>
""", unsafe_allow_html=True)

# -------------------- OVERVIEW --------------------

if page == "Overview":

    st.subheader("Your Daily Overview")
    st.caption("Illustrative sample data from the Apple Health workflow")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">👟 DAILY STEPS</div>
            <div class="metric-value">8,500</div>
            <div class="metric-note">Activity sample</div>
        </div>
        """, unsafe_allow_html=True)
        st.progress(step_progress)
        st.caption("85% of 10,000-step demo goal")

    with c2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">🌙 SLEEP DURATION</div>
            <div class="metric-value">7.5 hrs</div>
            <div class="metric-note">Sleep sample</div>
        </div>
        """, unsafe_allow_html=True)
        st.progress(sleep_progress)
        st.caption("94% of 8-hour demo goal")

    with c3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-label">🤖 AI HEALTH ENGINE</div>
            <div class="metric-value">Gemini</div>
            <div class="metric-note">Analysis available on demand</div>
        </div>
        """, unsafe_allow_html=True)
        st.progress(1.0)
        st.caption("AI analysis module connected")

    st.markdown("")

    left, right = st.columns([1.4, 1])

    with left:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.subheader("📊 Weekly Activity Trend")

        weekly_data = {
            "Day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
            "Steps": [6200, 7800, 8500, 7100, 9200, 10500, 8500]
        }

        st.bar_chart(
            weekly_data,
            x="Day",
            y="Steps"
        )

        st.caption("Illustrative weekly data — not actual Apple Health history.")

    with right:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.subheader("🎯 Daily Goals")

        st.write("👟 Steps")
        st.progress(step_progress)
        st.caption("8,500 / 10,000 steps")

        st.write("🌙 Sleep")
        st.progress(sleep_progress)
        st.caption("7.5 / 8 hours")

        st.write("✨ Overall")
        st.success("Sample health data loaded")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("")
    st.info(
        "This is a demonstration dashboard using sample data. "
        "Live Apple Health synchronization is not yet implemented."
    )

# -------------------- AI INSIGHTS --------------------

elif page == "AI Health Insights":

    st.subheader("🤖 AI Health Intelligence")
    st.write(
        "Let Gemini analyze activity and sleep data "
        "and generate personalized wellness suggestions."
    )

    st.markdown('<div class="panel">', unsafe_allow_html=True)

    st.markdown("### Current Analysis Input")
    a, b = st.columns(2)

    a.metric("Daily Steps", "8,500")
    b.metric("Sleep Duration", "7.5 hours")

    if st.button("✨ Generate AI Health Report", use_container_width=True):

        with st.spinner("Gemini is analyzing your health data..."):
            try:
                result = analyze_health_data(health_data)
                st.session_state["health_analysis"] = result
                st.success("Your AI analysis is ready!")

            except Exception as e:
                st.error(f"Analysis failed: {e}")

    st.markdown('</div>', unsafe_allow_html=True)

    if "health_analysis" in st.session_state:
        st.markdown("### 📋 Your Personalized Health Report")
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.markdown(st.session_state["health_analysis"])
        st.markdown('</div>', unsafe_allow_html=True)

# -------------------- EMAIL REPORTS --------------------

elif page == "Email Reports":

    st.subheader("📧 Intelligent Email Reports")
    st.write("Deliver Gemini-generated health insights directly to Gmail.")

    recipient = os.getenv("HEALTH_REPORT_EMAIL")

    st.markdown('<div class="panel">', unsafe_allow_html=True)

    st.markdown("### Report Configuration")

    if recipient:
        st.success("Gmail recipient configured")
        st.caption(f"Recipient: {recipient}")
    else:
        st.error("HEALTH_REPORT_EMAIL is missing from .env")

    if "health_analysis" not in st.session_state:
        st.warning("Generate a health analysis before sending a report.")

    elif st.button("📨 Send Health Report", use_container_width=True):

        if not recipient:
            st.error("Please configure HEALTH_REPORT_EMAIL.")

        else:
            try:
                with st.spinner("Sending your health report..."):
                    result = send_email(
                        recipient,
                        "Your AI Smartwatch Health Report",
                        st.session_state["health_analysis"]
                    )

                st.success("Health report delivered successfully!")
                st.write("Message ID:", result["message_id"])

            except Exception as e:
                st.error(f"Email delivery failed: {e}")

    st.markdown('</div>', unsafe_allow_html=True)

# -------------------- FOOTER --------------------

st.divider()

st.markdown(
    "<p style='text-align:center;color:#64748b;'>"
    "AI SMARTWATCH AGENT · Powered by Python, FastAPI and Google Gemini"
    "</p>",
    unsafe_allow_html=True
)
