import os
import requests

API_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

AI_AVAILABLE = True if OPENROUTER_API_KEY else False


def ask_ai(prompt):
    """
    Returns AI response if API works.
    Returns None if API fails (rate limit, timeout, model down).
    """
    if not AI_AVAILABLE:
        return None

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
        "max_tokens": 500,
        "temperature": 0.6
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=15)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
    except:
        pass

    return None  

