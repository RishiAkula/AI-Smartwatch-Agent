# ⌚ AI Smartwatch Agent – Health Intelligence AI

An AI-powered personal health assistant that transforms health activity data into meaningful insights and personalized wellness recommendations using Google Gemini.

## 🌟 Live Demo

**[Open Health Intelligence AI](https://health-intelligence-ai.streamlit.app/)**

## 🚀 Features

- **AI Health Analysis:** Uses Google Gemini to analyze health activity and sleep data.
- **Apple Health Integration:** Receives health information through a FastAPI webhook.
- **Automated Health Reports:** Sends AI-generated reports through Gmail API.
- **Interactive Dashboard:** Visualizes activity, sleep metrics and wellness insights using Streamlit.
- **AI News Assistant:** Retrieves and summarizes news using GNews and Gemini.

## 🛠️ Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| AI Model | Google Gemini |
| Backend | FastAPI |
| Frontend | Streamlit |
| Health Data | Apple Health Webhooks |
| Email | Gmail API |
| News | GNews API |
| Deployment | Streamlit Community Cloud |
| Version Control | Git and GitHub |

## 🏗️ Architecture

```text
Apple Health Data
       |
       v
FastAPI Webhook
       |
       v
Health Data Processing
       |
       v
Google Gemini AI
       |
       +------> AI Health Insights
       |
       +------> Gmail Health Reports

Streamlit Dashboard
       |
       +------> Activity Overview
       +------> Sleep Insights
       +------> AI Health Analysis
```

## 💻 Local Setup

1. Clone the repository:

```bash
git clone https://github.com/RishiAkula/AI-Smartwatch-Agent.git
cd AI-Smartwatch-Agent
```

2. Create and activate a virtual environment.

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure your API keys and credentials in a local `.env` file.

5. Run the dashboard:

```bash
streamlit run dashboard.py
```

## 🔐 Security

API keys, OAuth credentials and local environment files are excluded from version control. Configure secrets separately when deploying.

## 📌 Project Status

This is a working software prototype. The dashboard uses illustrative sample data; Apple Health webhook processing, Gemini analysis and Gmail reporting have been developed and tested separately. Continuous live health synchronization is not yet implemented.

## 👨‍💻 Author

**Rishi Akula**

M.Sc. Computer Science | AI & Software Development

---

*Built as a hands-on project exploring AI integration, backend development, automation and interactive data visualization.*
