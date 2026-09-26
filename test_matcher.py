from src.parser import extract_text_from_pdf
from src.llm_client import match_resume_to_jd

resume_text = extract_text_from_pdf("sample_resume.pdf")

jd_text = """
AI Engineer (Intern) - Botpresso
Build and improve internal tools and automation workflows.
Experiment with LLMs, AI Agents, Agentic AI, MCPs, APIs, and AI coding tools.
Work with Python/JavaScript, APIs, databases, web scraping, and browser automation.
Basic programming knowledge in Python, JavaScript, or similar.
Understanding of APIs, JSON, Git, databases, or web technologies.
Interest in AI, LLMs, Agents, automation, and emerging technologies.
"""

result = match_resume_to_jd(resume_text, jd_text)
print(result)