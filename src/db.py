import sqlite3
from datetime import datetime

DB_PATH = "match_history.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS match_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            resume_name TEXT,
            match_score INTEGER,
            matched_skills TEXT,
            missing_skills TEXT,
            summary TEXT
        )
    """)
    conn.commit()
    conn.close()

def log_match(resume_name, result):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO match_history (timestamp, resume_name, match_score, matched_skills, missing_skills, summary)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        datetime.now().isoformat(),
        resume_name,
        result["match_score"],
        ", ".join(result["matched_skills"]),
        ", ".join(result["missing_skills"]),
        result["summary"]
    ))
    conn.commit()
    conn.close()

def get_all_matches():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM match_history ORDER BY timestamp DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows