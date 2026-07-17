"""
PHQ-9 Assessment Engine

Author: Khansa Nurul Shafiyah

A Python implementation of the Patient Health Questionnaire-9 (PHQ-9)
for educational purposes.

Features
--------
- Score calculation
- Severity classification
- Item 9 clinical review flag
- Input validation
- Summary generation

Disclaimer
----------
This implementation is intended for educational purposes.
It is not a diagnostic tool and should not replace clinical judgment.
"""


def total_score(scores):
    """
    Calculate the total PHQ-9 score.

    Args:
        scores (list): A list of 9 PHQ-9 responses (0–3).

    Returns:
        int: The total PHQ-9 score.
    """
    total = 0

    for score in scores:
        total = total + score

    return total


def classify(score):
    """
    Classify the severity based on the total PHQ-9 score.

    Args:
        score (int): The total PHQ-9 score.

    Returns:
        str: The classification of PHQ-9 severity.
    """
    if 0 <= score <= 4:
        return "Minimal or None"
    elif 5 <= score <= 9:
        return "Mild"
    elif 10 <= score <= 14:
        return "Moderate"
    elif 15 <= score <= 19:
        return "Moderately Severe"
    elif 20 <= score <= 27:
        return "Severe"
    else:
        return "Invalid PHQ-9 Score"


def check_risk(scores):
    """
    Check for a positive response on PHQ-9 Item 9.

    Args:
        scores (list): A list of PHQ-9 responses (0–3).

    Returns:
        str: A message indicating whether the patient gave a positive response on PHQ-9 Item 9.
    """
    if scores[8] > 0:
        return "Positive response on PHQ-9 Item 9. Clinical review recommended."
    else:
        return "No positive response on PHQ-9 Item 9."


def is_complete(scores):
    """
    Check whether the PHQ-9 assessment is complete.

    Args:
        scores (list): A list of PHQ-9 responses.

    Returns:
        bool: True if there are exactly 9 responses and none of them is None; otherwise, False.
    """
    if len(scores) != 9:
        return False

    for score in scores:
        if score is None:
            return False

    return True


def is_valid(scores):
    """
    Validate the PHQ-9 responses.

    Args:
        scores (list): A list of PHQ-9 responses.

    Returns:
        bool: True if every response is between 0 and 3; otherwise, False.
    """
    for score in scores:
        if not 0 <= score <= 3:
            return False

    return True


def assess_patient(scores):
    """
    Assess the PHQ-9 responses and generate a screening summary.

    Args:
        scores (list): A list of PHQ-9 responses.

    Returns:
        str: A formatted summary of the PHQ-9 assessment.
    """
    if not is_complete(scores):
        return "Assessment Incomplete. Please answer all questions."

    if not is_valid(scores):
        return "Invalid PHQ-9 responses. Each answer must be 0, 1, 2, or 3."

    total = total_score(scores)
    category = classify(total)
    clinical_review = check_risk(scores)

    return generate_summary(total, category, clinical_review)


def generate_summary(total, category, clinical_review):
    """
    Generate a formatted summary of the PHQ-9 assessment.

    Args:
        total (int): The total PHQ-9 score.
        category (str): The PHQ-9 severity classification.
        clinical_review (str): The clinical review message for PHQ-9 Item 9.

    Returns:
        str: A formatted PHQ-9 assessment summary.
    """
    return f"""
==============================
PHQ-9 SCREENING SUMMARY
==============================

PHQ-9 Score: {total}

Severity: {category}

Clinical Review:
{clinical_review}

Disclaimer:
This is a screening result only and does not establish a diagnosis.

"""