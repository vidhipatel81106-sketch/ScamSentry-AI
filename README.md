# 🛡️ ScamSentry AI
### Your Digital Guardian Against Online Scams

ScamSentry AI is an AI-powered web application designed to help users identify potential online scams, understand suspicious messages, and improve their cybersecurity awareness.

## 📌 Project Overview

Online scams such as phishing messages, fake job offers, fraudulent banking messages, and UPI fraud are increasing. ScamSentry AI helps users recognize possible threats by analyzing suspicious messages and providing risk assessments, warning signs, and safety recommendations.

## 🎯 Objectives

- Detect potential scam messages using Artificial Intelligence.
- Identify suspicious URLs and link patterns.
- Provide risk scores and warning signs.
- Offer practical safety recommendations.
- Educate users about common online scams.
- Provide an AI-powered cybersecurity chatbot.

## ✨ Features

1. **AI Scam Detection:** Analyzes submitted messages and displays risk scores, risk levels, categories, warning signs, and recommendations.
2. **URL Safety Checker:** Checks URLs for suspicious patterns.
3. **User Authentication:** Provides registration and login functionality.
4. **Scan History:** Stores scan records separately for individual users.
5. **Dashboard:** Displays scan statistics and information.
6. **PDF Reports:** Generates downloadable scan reports.
7. **Scam Awareness Center:** Provides cybersecurity information and safety tips.
8. **AI Chatbot:** Answers questions about phishing, UPI fraud, OTP safety, and online scams.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Web application framework |
| Google Gemini API | AI-powered analysis and chatbot |
| SQLite | Database management |
| ReportLab | PDF report generation |
| Pandas | Data handling |
| Cursor AI | AI-assisted coding |

## 📁 Project Structure

```text
ScamSentry-AI/
│
├── app.py
├── auth.py
├── database.py
├── requirements.txt
├── README.md
│
└── .streamlit/
    └── secrets.toml
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the Project Folder

```bash
cd ScamSentry-AI
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure the Gemini API Key

Create a `.streamlit/secrets.toml` file and add:

```toml
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"
```

Replace the placeholder with your own Gemini API key. Never upload this file or share your API key publicly.

### 7. Run the Application

```bash
python -m streamlit run app.py
```

The application will open in your browser.

## 🧪 Testing

The application was tested with different types of inputs, including:

- Suspicious banking messages.
- Fake job offer messages.
- Potential phishing messages.
- Normal messages.
- Suspicious URL patterns.
- Chatbot cybersecurity questions.
- User registration and login.
- User-specific scan history.
- PDF report generation.

AI-generated risk scores are indicators and should not be treated as proof that a message or website is fraudulent or safe.

## 🔐 Security Considerations

- Passwords are stored using password hashing.
- API keys are kept in Streamlit secrets.
- Scan history is associated with individual user accounts.
- Submitted messages are treated as untrusted input.
- The URL checker uses pattern-based checks and does not guarantee website safety.

## 🇮🇳 Cybercrime Reporting in India

If you experience financial cyber fraud:

- Call **1930** promptly.
- Report the incident at https://cybercrime.gov.in/

## 🚀 Future Enhancements

- Integration with verified threat intelligence services.
- Multilingual scam detection.
- Improved detection using larger datasets.
- Advanced URL reputation checking.
- Additional cybersecurity awareness resources.

## 👩‍💻 Project Information

**Project Name:** ScamSentry AI  
**Project Title:** Your Digital Guardian Against Online Scams  
**Domain:** Artificial Intelligence and Cybersecurity

Developed as a second-year engineering college project.

---

**Disclaimer:** ScamSentry AI is an educational cybersecurity awareness project. Its AI analysis and URL checks may not detect every scam. Users should independently verify suspicious messages and websites.