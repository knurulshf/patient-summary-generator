def determine_followup(phq9_score, gad7_score, item9_response):
    if item9_response > 0:
        return "Safety assessment recommended"
    elif phq9_score >= 10 or gad7_score >= 10:
        return "Clinical follow-up recommended"
    else:
        return "Routine screening follow-up"