def evaluate_answer(answer):
    if not answer.strip():
        return "❌ No answer provided.\nConfidence Score: 0/10"

    words = len(answer.split())

    if words < 10:
        score = 4
        remark = "Answer is too short."
    elif words < 30:
        score = 7
        remark = "Good answer, but can improve."
    else:
        score = 9
        remark = "Excellent explanation."

    return f"{remark}\nConfidence Score: {score}/10"


def evaluate_code(code):
    if not code.strip():
        return "❌ No code submitted.\nScore: 0/10"

    lines = code.count("\n") + 1

    if lines < 5:
        score = 5
        remark = "Code is too short."
    elif lines < 15:
        score = 8
        remark = "Good code structure."
    else:
        score = 9
        remark = "Well-written code."

    return f"{remark}\nCode Quality Score: {score}/10"
