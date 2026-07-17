# Patient Summary Generator

A Python application that generates a patient summary using PHQ-9 and GAD-7 assessment modules.

## Overview

This project integrates the **PHQ-9 Assessment Engine** and **GAD-7 Assessment Engine** to generate a structured patient summary.

The application validates questionnaire responses, calculates assessment scores, classifies symptom severity, identifies suicide risk based on the PHQ-9 Item 9 response, and displays a formatted patient summary.

This project is intended as a learning exercise in Python programming, modular software design, and clinical decision-support workflows.

---

## Related Projects

- [PHQ-9 Assessment Engine](https://github.com/knurulshf/phq9-assessment-engine)
- [GAD-7 Assessment Engine](https://github.com/knurulshf/gad7-assessment-engine)

---

## Features

* PHQ-9 assessment integration
* GAD-7 assessment integration
* Input validation
* PHQ-9 suicide risk flag
* Structured patient summary generation
* Modular project structure

---

## Project Structure

```text
patient-summary-generator/
│
├── main.py          # Patient summary generator
├── phq9.py          # PHQ-9 assessment module
├── gad7.py          # GAD-7 assessment module
├── README.md
├── LICENSE
└── .gitignore
```

---

## Example Output

```text
==========================
PATIENT SUMMARY
==========================

Patient ID: 101
Name: Alya
Age: 22
Doctor: Dr. A

PHQ-9 Score: 18
PHQ-9 Severity: Moderately Severe
Risk: Positive response on PHQ-9 Item 9. Clinical review recommended.

GAD-7 Score: 14
GAD-7 Severity: Moderate Anxiety
```

---

## Requirements

- Python 3.10 or later

This project uses only Python's standard library and the included PHQ-9 and GAD-7 modules.

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/knurulshf/patient-summary-generator.git
```

Navigate to the project directory:

```bash
cd patient-summary-generator
```

Run the application:

```bash
python main.py
```

---

## Learning Objectives

This project demonstrates:

* Python functions
* Modular programming
* Module imports
* Dictionaries and lists
* Input validation
* Code reuse
* Software organization

---

## Disclaimer

This project is intended for educational purposes only.

It is **not** a diagnostic tool and should **not** replace clinical judgment or professional medical assessment.

---

## Future Improvements

- Interactive patient input
- Streamlit web application
- SQLite patient database
- Integrated mental health assessment MVP
- AI-assisted patient summaries
- Hospital workflow integration

---

## Author

**Khansa Nurul Shafiyah**
