# ⌚ AI Smartwatch Agent – Health Intelligence AI

An AI-powered personal health assistant that transforms activity and sleep data into meaningful insights and personalized wellness recommendations using **Google Gemini**.

\<p align="center">   \<a href="[https://health-intelligence-ai.streamlit.app/](https://health-intelligence-ai.streamlit.app/)">     \<strong>🚀 Launch Live Application\</strong>   \</a>   &nbsp; | &nbsp;   \<a href="[https://github.com/RishiAkula/AI-Smartwatch-Agent](https://github.com/RishiAkula/AI-Smartwatch-Agent)">     \<strong>💻 View Source Code\</strong>   \</a> \</p>

---

## 🌟 Overview

AI Smartwatch Agent is a Python-based health intelligence prototype combining AI-powered analysis, backend APIs, email automation and an interactive dashboard.

The project explores how wearable health information can be transformed into understandable insights and actionable wellness recommendations.

## 🚀 Features

- **AI Health Analysis:** Google Gemini analyzes activity and sleep information and generates personalized wellness recommendations.
- **Apple Health Integration:** FastAPI webhook receives Apple Health data payloads.
- **Automated Health Reports:** Gmail API integration sends AI-generated health reports.
- **Interactive Dashboard:** Streamlit dashboard presents activity metrics, sleep information and health insights.
- **AI News Assistant:** Retrieves news using GNews and generates summaries with Gemini.

## 🖥️ Application Preview

**Live Demo:** [https://health-intelligence-ai.streamlit.app/](https://health-intelligence-ai.streamlit.app/)

The dashboard includes:

- Daily activity overview
- Sleep duration monitoring
- AI-generated health insights
- Email report configuration

*The current dashboard uses illustrative sample data.*

## 🛠️ Technology Stack

| Component               | Technology                |
| ----------------------- | ------------------------- |
| Programming Language    | Python                    |
| AI Model                | Google Gemini             |
| Backend Framework       | FastAPI                   |
| Frontend / Dashboard    | Streamlit                 |
| Health Data Integration | Apple Health Webhooks     |
| Email Automation        | Gmail API                 |
| News Retrieval          | GNews API                 |
| Deployment              | Streamlit Community Cloud |
| Version Control         | Git and GitHub            |

## 🏗️ System Architecture

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
                Google Gemini
                     |
              +------+------+
              |             |
              v             v
        Health Insights   Gmail Reports


             Streamlit Dashboard
                     |
          +----------+----------+
          |          |          |
          v          v          v
        Activity   Sleep     AI Health
        Overview   Insights  Analysis


             AI News Assistant
                     |
                     v
                 GNews API
                     |
                     v
                Google Gemini
                     |
                     v
               News Summaries
```

## 💻 Local Installation

### 1. Clone the repository

```bash
git clone https://github.com/RishiAkula/AI-Smartwatch-Agent.git
cd AI-Smartwatch-Agent
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root and configure the required API keys and settings.

Example:

```env
GEMINI_API_KEY=your_gemini_api_key
GNEWS_API_KEY=your_gnews_api_key
HEALTH_REPORT_EMAIL=your_email_address
```

Configure Gmail OAuth credentials separately when using the email integration.

**Never commit API keys, OAuth credentials or token files to GitHub.**

### 5. Run the dashboard

```bash
streamlit run dashboard.py
```

Open the local URL provided by Streamlit in your browser.

## 🔐 Security

- API keys are stored outside source control.
- Local environment files and OAuth credentials are excluded from Git.
- Streamlit Cloud secrets are used for deployment configuration.
- Health information should only be shared with authorized services and recipients.

## 📌 Project Status

This project is a working software prototype.

| Feature                                | Status                      |
| -------------------------------------- | --------------------------- |
| Streamlit dashboard                    | Deployed                    |
| Gemini health analysis                 | Integrated                  |
| Apple Health webhook                   | Tested with sample payloads |
| Gmail health reporting                 | Tested locally              |
| AI News Assistant                      | Integrated                  |
| Continuous live health synchronization | Not yet implemented         |
| Cloud-based Gmail report delivery      | Not yet configured          |

**Important:** The public dashboard currently displays illustrative sample data. It does not represent continuous live synchronization with a wearable device.

## 🔮 Future Improvements

- Continuous wearable health data synchronization
- Personalized activity and sleep goals
- Historical health trends and visual analytics
- Secure cloud-based Gmail OAuth integration
- More advanced AI-generated wellness insights

## 👨‍💻 Author

**Rishi Akula**

M.Sc. Computer Science | AI & Software Development

- GitHub: [@RishiAkula](https://github.com/RishiAkula)
- Project: [AI-Smartwatch-Agent](https://github.com/RishiAkula/AI-Smartwatch-Agent)
- Live Application: [Health Intelligence AI](https://health-intelligence-ai.streamlit.app/)

---

*Built as a hands-on project exploring Generative AI, wearable health data, backend development, automation and interactive data visualization.*
