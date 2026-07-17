"""
Patient Summary Generator

Author: Khansa Nurul Shafiyah

A Python application that generates a patient summary using
PHQ-9 and GAD-7 assessment modules.

Features:
---------
- Patient summary generation
- PHQ-9 and GAD-7 integration
- Input validation
- Suicide risk flag

Disclaimer:
-----------
This project is intended for educational purposes.
It is not a diagnostic tool and should not replace
clinical judgment.
"""

import phq9
import gad7


def generate_summary(patient):
    """
    Generate and display a patient summary using PHQ-9 and GAD-7 responses.

    The function validates the questionnaire responses, calculates
    PHQ-9 and GAD-7 scores, classifies severity, checks suicide
    risk using the PHQ-9 module, and prints a formatted summary.

    Args:
        patient (dict): A dictionary containing patient information
            and questionnaire responses.
    """
    phq9_responses = patient["phq9_responses"]
    gad7_responses = patient["gad7_responses"]

    if not phq9.is_complete(phq9_responses):
        print("Incomplete PHQ-9 responses: exactly 9 responses are required")
        return

    if not phq9.is_valid(phq9_responses):
        print("Invalid PHQ-9 responses: each answer must be 0, 1, 2, or 3")
        return

    if not gad7.is_complete(gad7_responses):
        print("Incomplete GAD-7 responses: exactly 7 responses are required")
        return

    if not gad7.is_valid(gad7_responses):
        print("Invalid GAD-7 responses: each answer must be 0, 1, 2, or 3")
        return

    phq9_score = phq9.total_score(phq9_responses)
    phq9_severity = phq9.classify(phq9_score)
    risk = phq9.check_risk(phq9_responses)

    gad7_score = gad7.total_score(gad7_responses)
    gad7_severity = gad7.classify(gad7_score)

    print("==========================")
    print("PATIENT SUMMARY")
    print("==========================")
    print()
    print("Patient ID:", patient["patient_id"])
    print("Name:", patient["name"])
    print("Age:", patient["age"])
    print("Doctor:", patient["doctor"])
    print()
    print("PHQ-9 Score:", phq9_score)
    print("PHQ-9 Severity:", phq9_severity)
    print("Risk:", risk)
    print()
    print("GAD-7 Score:", gad7_score)
    print("GAD-7 Severity:", gad7_severity)
    print()


patient1 = {
    "patient_id": 101,
    "name": "Alya",
    "age": 22,
    "doctor": "Dr. A",
    "phq9_responses": [2, 2, 2, 2, 2, 2, 2, 2, 2],
    "gad7_responses": [2, 2, 2, 2, 2, 2, 2]
}

patient2 = {
    "patient_id": 102,
    "name": "Budi",
    "age": 35,
    "doctor": "Dr. B",
    "phq9_responses": [1, 1, 1, 1, 1, 1, 1, 1, 0],
    "gad7_responses": [1, 1, 1, 1, 1, 0, 0]
}

patient_records = [patient1, patient2]

if __name__ == "__main__":
    for patient in patient_records:
        generate_summary(patient)