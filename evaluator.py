def evaluate_answer(answer):
    if not answer.strip():
        return (
            "❌ No response detected.\n\n"
            "Feedback:\n"
            "You did not provide an answer. In interviews, even a brief structured response "
            "is better than silence. Try to communicate your thoughts clearly.\n\n"
            "Confidence Score: 0/10"
        )

    text = answer.lower()
    word_count = len(answer.split())

    # ---------- COMMON KEYWORDS ----------
    leadership = ["lead", "team", "responsibility", "initiative"]
    learning = ["learn", "improve", "adapt", "training"]
    problem = ["challenge", "problem", "issue", "solution"]
    future = ["future", "career", "goal", "growth"]
    pressure = ["pressure", "stress", "deadline"]
    motivation = ["motivated", "passion", "interest"]

    score = 5
    remarks = []

    # ---------- ANALYSIS ----------
    if any(k in text for k in leadership):
        remarks.append("You demonstrated leadership awareness.")
        score += 1

    if any(k in text for k in learning):
        remarks.append("You showed a willingness to learn and adapt.")
        score += 1

    if any(k in text for k in problem):
        remarks.append("You explained how you handle challenges.")
        score += 1

    if any(k in text for k in future):
        remarks.append("Your answer reflects future-oriented thinking.")
        score += 1

    if any(k in text for k in pressure):
        remarks.append("You addressed handling pressure effectively.")
        score += 1

    if any(k in text for k in motivation):
        remarks.append("Your motivation for work is clearly expressed.")
        score += 1

    # ---------- LENGTH BASED REFINEMENT ----------
    if word_count < 15:
        remarks.append("The answer is too short. Interviewers expect structured explanations.")
        score -= 1
    elif word_count > 50:
        remarks.append("Your explanation is detailed and well-articulated.")
        score += 1

    score = max(3, min(score, 9))

    # ---------- FINAL FEEDBACK ----------
    feedback = (
        "Feedback:\n"
        + " ".join(remarks)
        + "\n\n"
        "Overall Evaluation:\n"
        "Your response is relevant and demonstrates professional thinking. "
        "With better structure and clearer examples, it can be even stronger.\n\n"
        f"Confidence Score: {score}/10"
    )

    return feedback


def evaluate_code(code):
    if not code.strip():
        return (
            "❌ No code submitted.\n\n"
            "Feedback:\n"
            "You did not provide a solution. Interviewers expect at least a basic approach "
            "or pseudocode even if the full solution is incomplete.\n\n"
            "Code Quality Score: 0/10"
        )

    text = code.lower()
    lines = code.count("\n") + 1

    score = 5
    remarks = []

    # ---------- LOGIC CHECKS ----------
    if "for" in text or "while" in text:
        remarks.append("Looping logic is correctly identified.")
        score += 1

    if "if" in text:
        remarks.append("Conditional logic is appropriately used.")
        score += 1

    if "return" in text:
        remarks.append("Function return logic is present.")
        score += 1

    if any(k in text for k in ["def", "function", "int", "main"]):
        remarks.append("Proper function structure is used.")
        score += 1

    if any(k in text for k in ["sort", "reverse", "palindrome", "factorial", "fibonacci"]):
        remarks.append("Problem-specific logic is applied.")
        score += 1

    # ---------- STRUCTURE ----------
    if lines < 5:
        remarks.append("The solution is very short and may miss edge cases.")
        score -= 1
    elif lines > 15:
        remarks.append("The solution is well-structured and readable.")
        score += 1

    score = max(4, min(score, 9))

    # ---------- FINAL FEEDBACK ----------
    feedback = (
        "Code Review Feedback:\n"
        + " ".join(remarks)
        + "\n\n"
        "Overall Evaluation:\n"
        "Your solution demonstrates logical thinking and an understanding of core programming concepts. "
        "With better variable naming and edge-case handling, this would be production-ready.\n\n"
        f"Code Quality Score: {score}/10"
    )

    return feedback

