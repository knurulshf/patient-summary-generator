"""
GAD-7 Assessment Engine

Author: Khansa Nurul Shafiyah

A Python implementation of the Generalized Anxiety Disorder (GAD-7) questionnaire for educational purposes.

Features:
---------
- Score calculation
- Severity classification
- Input validation
- Summary generation

Disclaimer:
-----------
This implementation is intended for educational purposes.
It is not a diagnostic tool and should not replace clinical judgment.
"""


def total_score(scores):
    """
    Calculate the total GAD-7 score.

    Args:
        scores (list): A list of 7 GAD-7 responses (0–3).

    Returns:
        int: The total GAD-7 score.
    """
    total = 0

    for score in scores:
        total = total + score

    return total


def classify(score):
    """
    Classify the GAD-7 score into an anxiety severity category.

    Args:
        score (int): The GAD-7 score.

    Returns:
        str: Anxiety severity classification
    """
    if 0 <= score <= 4:
        return "Minimal Anxiety"
    elif 5 <= score <= 9:
        return "Mild Anxiety"
    elif 10 <= score <= 14:
        return "Moderate Anxiety"
    elif 15 <= score <= 21:
        return "Severe Anxiety"
    else:
        return "Invalid score"


def is_complete(scores):
    """
    Check whether the GAD-7 responses are complete (7 in total, no None answers).

    Args:
        scores (list): A list of 7 GAD-7 responses.

    Returns:
        bool: True if the GAD-7 score is complete, otherwise False.
    """
    if len(scores) != 7:
        return False

    for score in scores:
        if score is None:
            return False

    return True


def is_valid(scores):
    """
    Check whether the GAD-7 responses are valid.

    Args:
        scores (list): A list of 7 GAD-7 responses.

    Returns:
        bool: True if every response is between 0 and 3, otherwise False.
    """
    for score in scores:
        if not 0 <= score <= 3:
            return False

    return True


def assess_patient(scores):
    """
    Assess the GAD-7 responses and generate a screening summary.

    Args:
        scores (list): A list of GAD-7 responses.

    Returns:
        str: A formatted summary of the GAD-7 assessment.
    """
    if not is_complete(scores):
        return "Questionnaire incomplete."
    if not is_valid(scores):
        return "Questionnaire invalid. Each answer must be 0, 1, 2, or 3."

    total = total_score(scores)
    category = classify(total)

    return generate_summary(total, category)


def generate_summary(total, category):
    """
    Generate a formatted summary of the GAD-7 assessment.

    Args:
        total (int): The total GAD-7 score.
        category (str): The GAD-7 severity classification.

    Returns:
        str: A formatted GAD-7 assessment summary.
    """
    return f"""
==============================
GAD-7 SCREENING SUMMARY
==============================

GAD-7 Score: {total}
Severity: {category}

Disclaimer:
This is a screening result only and does not establish a diagnosis.

"""