def get_questions(round_type, ai_mode=False):
    if ai_mode:
        return [
            f"{i+1}. {q}" for i, q in enumerate(_offline_questions(round_type))
        ]
    else:
        return _offline_questions(round_type)


def _offline_questions(round_type):
    if round_type == "HR Interview":
        return [
            "Tell me about yourself.",
            "What are your strengths?",
            "What are your weaknesses?",
            "Why should we hire you?",
            "Where do you see yourself in 5 years?",
            "Describe a challenging situation you handled.",
            "How do you handle pressure?",
            "What motivates you?",
            "Are you willing to learn new technologies?",
            "Do you have any questions for us?"
        ]

    if round_type == "Technical Interview":
        return [
            "What is OOPS and its principles?",
            "Difference between stack and queue.",
            "What is a database index?",
            "Explain normalization.",
            "What is operating system?",
            "Difference between compiler and interpreter.",
            "Explain SDLC.",
            "What is time complexity?",
            "What is REST API?",
            "Explain MVC architecture."
        ]

    if round_type == "Coding Round":
        return [
            "Write a program to reverse a string.",
            "Check whether a number is palindrome.",
            "Find the largest element in an array.",
            "Write a program for factorial using recursion.",
            "Check if a number is prime.",
            "Find Fibonacci series up to N.",
            "Sort an array using bubble sort.",
            "Count vowels in a string.",
            "Find second largest element in an array.",
            "Reverse an array."
        ]

    return []


def ai_evaluate_answer(question, answer):
    return f"""
Question: {question}
Candidate Answer: {answer}

Give:
1) Short feedback
2) Confidence score out of 10
"""


def ai_evaluate_code(code):
    return f"""
Analyze the following code:
{code}

Check:
- Syntax errors
- Logical mistakes
- Time complexity
- Improvements
"""
