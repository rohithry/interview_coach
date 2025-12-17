import os
import requests

API_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

AI_AVAILABLE = True if OPENROUTER_API_KEY else False

def ask_ai(prompt):
    if not AI_AVAILABLE:
        return "AI not available."

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "nex-agi/deepseek-v3.1-nex-n1:free",
        "messages": [
            {"role": "system", "content": "You are a professional interviewer and evaluator."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 700,
        "temperature": 0.6
    }

    r = requests.post(API_URL, headers=headers, json=payload)
    if r.status_code == 200:
        return r.json()["choices"][0]["message"]["content"]

    return "AI error"
