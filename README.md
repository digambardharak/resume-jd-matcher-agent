
# 🎯 AI Resume-JD Matcher Agent

I built this project to solve a problem I kept running into during my own job search: it's hard to know exactly how well a resume matches a job description, and even harder to know what to learn next to close the gap. So I built an AI agent that does both — instantly.

It reads a resume, compares it against a job description using an LLM, scores the match, and then goes one step further: it automatically searches the web for real learning resources to help close the missing skills. That last part is what makes it an *agent* rather than just a chatbot wrapper — it perceives, decides, and acts on its own.

---

## What It Does

- Upload a resume (PDF) and paste any job description
- Google Gemini reads both and compares them intelligently — not just keyword matching
- Get back a match score (0–100), a list of matched skills, a list of missing skills, and a short summary
- For every missing skill, the agent automatically searches the web (via Tavily) and suggests 2–3 real learning resources
- Every analysis is saved to a local database, so you can track your progress over time

---

## Why I Built It

Most resume-JD matching tools just do keyword matching, which misses context. I wanted something that actually *understands* both documents the way a recruiter would, and then goes a step further by helping the candidate act on the gaps it finds — which is exactly the kind of "LLM + agent" workflow I wanted hands-on experience building.

---

## Tech Stack

| Layer              | Technology                                  |
| ------------------ | ------------------------------------------- |
| Language           | Python                                      |
| LLM                | Google Gemini (`google-genai` SDK)        |
| Agent / Web Search | Tavily Search API                           |
| PDF Parsing        | pdfplumber                                  |
| Interface          | Streamlit                                   |
| Database           | SQLite                                      |
| Config             | python-dotenv (for secure API key handling) |

---

## How It Works

1. You upload a resume (PDF) and paste a job description
2. The app extracts plain text from the PDF using `pdfplumber`
3. The resume text and JD are sent to Gemini with a prompt that forces clean, structured JSON output
4. The response is parsed into a match score, matched skills, missing skills, and a summary
5. For each missing skill, an agent step calls the Tavily API and pulls back real learning resources
6. Everything is displayed in a simple Streamlit interface, and the result is logged to a local SQLite database

---

## Screenshots

**A real match result**
![Match Result](screenshots/match_result.png)

**Input validation — no crashes on missing input**
![Empty State Warning](screenshots/empty_state.png)

---

## Getting Started

**1. Clone the repo**

git clone https://github.com/digambardharak/resume-jd-matcher-agent.git
cd resume-jd-matcher-agent

**2. Create and activate a virtual environment**

python -m venv venv
venv\Scripts\activate # Windows
source venv/bin/activate # Mac/Linux

**3. Install the dependencies**

pip install -r requirements.txt

**4. Add your own API keys**

Create a `.env` file in the project root:

GEMINI_API_KEY=your_gemini_key_here
TAVILY_API_KEY=your_tavily_key_here

Both Gemini and Tavily offer free API keys — no credit card required.

**5. Run the app**

streamlit run app.py

---

## Project Structure

resume-jd-matcher-agent/
├── app.py # Streamlit UI
├── src/
│ ├── parser.py # PDF text extraction
│ ├── llm_client.py # Gemini API calls + JSON parsing
│ ├── agent.py # Tavily search for skill-gap resources
│ └── db.py # SQLite logging
├── requirements.txt
└── README.md

---

## What I Learned

This was my first real hands-on project working directly with LLM APIs and agentic workflows. Along the way I worked through:

- Designing prompts that reliably return structured JSON instead of free text
- Building a simple perceive → decide → act agent loop
- Integrating two different external APIs (Gemini + Tavily) into one working pipeline
- Handling real production issues — rate limits, deprecated SDKs, and shifting model versions — the same kind of debugging this internship role asks for

---

## Future Improvements

- [ ] Support more resume formats (DOCX)
- [ ] Compare one resume against multiple job descriptions in a batch
- [ ] Export the full match report as a downloadable PDF
- [ ] Deploy publicly with a shareable live link

---

## Author

**Digambar Dharak**
📧 digambardharak562002@gmail.com
🔗 [LinkedIn](https://linkedin.com/in/digambardharak) · [GitHub](https://github.com/digambardharak)
