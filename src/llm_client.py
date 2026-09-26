import os
import json
import time
from dotenv import load_dotenv
from google import genai
from google.genai.errors import ServerError

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def match_resume_to_jd(resume_text, jd_text, max_retries=4):
    """Send resume + JD to Gemini and get back a structured match report."""

    prompt = f"""
You are a resume-screening assistant. Compare the RESUME to the JOB DESCRIPTION below.

Return ONLY valid JSON, no extra text, no markdown formatting, in exactly this structure:
{{
  "match_score": <integer 0-100>,
  "matched_skills": ["skill1", "skill2"],
  "missing_skills": ["skill1", "skill2"],
  "summary": "<one short sentence on overall fit>"
}}

RESUME:
{resume_text}

JOB DESCRIPTION:
{jd_text}
"""

    for attempt in range(1, max_retries + 1):
        try:
            response = client.models.generate_content(
                model="gemini-3.1-flash-lite",
                contents=prompt
            )
            break
        except ServerError as e:
            print(f"Attempt {attempt} failed (server busy). Retrying in 5 seconds...")
            if attempt == max_retries:
                print("Gemini is still overloaded after several tries. Try again in a minute.")
                return None
            time.sleep(5)

    raw_text = response.text.strip()

    if raw_text.startswith("```"):
        raw_text = raw_text.strip("`")
        raw_text = raw_text.replace("json", "", 1).strip()

    try:
        result = json.loads(raw_text)
    except json.JSONDecodeError:
        print("Could not parse JSON. Raw response was:")
        print(raw_text)
        return None

    return result