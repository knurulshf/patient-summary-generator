import sqlite3
from datetime import datetime


def create_table():
    conn = sqlite3.connect("assessments.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS assessments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id TEXT,
        name TEXT,
        age INTEGER,
        doctor TEXT,
        phq9_score INTEGER,
        gad7_score INTEGER,
        phq9_severity TEXT,
        gad7_severity TEXT,
        item9_flag INTEGER,
        followup_result TEXT,
        assessment_date TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_assessment(
        patient_id,
        name,
        age,
        doctor,
        phq9_score,
        gad7_score,
        phq9_severity,
        gad7_severity,
        item9_flag,
        followup_result
):
    conn = sqlite3.connect("assessments.db")
    cursor = conn.cursor()

    assessment_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
    INSERT INTO assessments (
        patient_id,
        name,
        age,
        doctor,
        phq9_score,
        gad7_score,
        phq9_severity,
        gad7_severity,
        item9_flag,
        followup_result,
        assessment_date
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        patient_id,
        name,
        age,
        doctor,
        phq9_score,
        gad7_score,
        phq9_severity,
        gad7_severity,
        item9_flag,
        followup_result,
        assessment_date
    ))

    conn.commit()
    conn.close()


def get_assessments():
    conn = sqlite3.connect("assessments.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM assessments
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows


def delete_assessment(assessment_id):
    conn = sqlite3.connect("assessments.db")
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM assessments
    WHERE id = ?
    """, (assessment_id,))

    conn.commit()
    conn.close()


def update_assessment(
        assessment_id,
        patient_id,
        name,
        age,
        doctor,
        phq9_score,
        gad7_score,
        phq9_severity,
        gad7_severity,
        item9_flag,
        followup_result
):
    conn = sqlite3.connect("assessments.db")
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE assessments
    SET patient_id = ?,
        name = ?,
        age = ?,
        doctor = ?,
        phq9_score = ?,
        gad7_score = ?,
        phq9_severity = ?,
        gad7_severity = ?,
        item9_flag = ?,
        followup_result = ?
    WHERE id = ?
    """, (
        patient_id,
        name,
        age,
        doctor,
        phq9_score,
        gad7_score,
        phq9_severity,
        gad7_severity,
        item9_flag,
        followup_result,
        assessment_id
    ))

    conn.commit()
    conn.close()


create_table()